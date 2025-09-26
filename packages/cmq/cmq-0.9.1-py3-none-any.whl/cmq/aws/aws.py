import boto3
import re

from botocore.exceptions import ClientError
from datetime import datetime, timedelta
from functools import partial
from matplotlib import pyplot as plt
from typing import Any

from cmq.base import Resource
from cmq.iterator import UnknownSizeIterator, InfiniteAtpbar, Atpbar


class AWSClientInterface:

    def __init__(self):
        self._service = ""
        self._list_function = ""
        self._list_key = ""
        self._list_parameters = {}
        self._list_paginated = True

    @property
    def _desc(self) -> str:
        return f"{self._service}_{self._resource}"

    def __call__(self, **kwargs) -> "AWSClientInterface":
        self._list_parameters = kwargs
        return self

    def get_client(self, context, service = None) -> boto3.client:
        return context["aws_session"].client(service or self._service)

    def get_parameters(self, context: dict) -> dict:
        return self._list_parameters

    def traverse(self, context: dict) -> None:
        for resource in self.bar(context, self.get(context), desc=f"{self._desc} traverse"):
            context.update({
                f"{self._desc}": resource
            })
            self._traverse(context)

    def get_paged_results(self, page) -> list:
        return page.get(self._list_key, []) if self._list_key else self._get_results(page)

    def _get_pages(self, context) -> Any:
        client = self.get_client(context)
        paginator = client.get_paginator(self._list_function)
        return paginator.paginate(**self.get_parameters(context))

    def _get(self, context) -> list:
        """
        Retrieves resources from AWS and processes them through the pipeline.

        Args:
            context (dict): The context containing session information.

        Returns:
            list: List of resources
        """
        resources = []
        try:
            if self._list_paginated:
                resources = self.paginate(context)
                resources = [r if isinstance(r, dict) else {"resource": r} for r in resources]
            else:
                client = self.get_client(context)
                page = getattr(client, self._list_function)(**self.get_parameters(context))
                resources = self.get_paged_results(page)
            return resources
        except Exception as ex:
            return [{"error": str(ex)}]

    def get(self, context):
        """
        Retrieves resources and processes them through the pipeline.

        Args:
            context (dict): The context containing session information.

        Returns:
            list: Processed list of resources.
        """
        resources = self._get(context)
        return self._process_pipeline(resources, context)

    def _get_results(self, page) -> list | None:
        for value in page.values():
            if isinstance(value, list):
                return value
        return None


class TagResourceInterface:

    def __init__(self):
        self._tag_function = ""
        self._tag_function_key = ""
        self._tag_resource_key = ""

    def tags(self) -> "TagResourceInterface":
        """
        Adds a tag operation to the pipeline that will retrieve tags for the resources.

        Returns:
            TagResourceInterface: The updated resource object.
        """
        self._pipeline.append(self._tag_resources)
        return self

    def _get_tag_resource_identifier(self, context, resource) -> str:
        return resource[self._tag_resource_key]

    def _tag_resources(self, resources, context) -> list:
        if self._tag_function:
            client = self.get_client(context)
            for resource in self.bar(context, resources, "tags"):
                if isinstance(resource, dict):
                    try:
                        tag_function = getattr(client, self._tag_function)
                        tag_identifier = self._get_tag_resource_identifier(context, resource)
                        result = tag_function(**{self._tag_function_key: tag_identifier})
                        result_tags = self._get_tag_from_result(result)
                        tags = self._format_tags(result_tags)
                        resource.update(tags)
                    except ClientError as ex:
                        resource.update({"Tags": {"error": str(ex)}})
        return resources

    def _get_tag_from_result(self, result) -> list:
        return self._get_results(result) or []

    def _format_tags(self, tags) -> dict:
        return {"Tags": {tag["Key"]: tag["Value"] for tag in tags}}


class DescribeResourceInterface:

    def __init__(self):
        self._describe_function = ""
        self._describe_function_key = ""
        self._describe_resource_key = ""

    def describe(self) -> "DescribeResourceInterface":
        """
        Adds a describe operation to the pipeline that will retrieve details for the resources.

        Returns:
            DescribeResourceInterface: The updated resource object.
        """
        self._pipeline.append(self._describe_resources)
        return self

    def _get_describe_resource_identifier(self, context, resource) -> str:
        return resource[self._describe_resource_key]

    def _describe_resources(self, resources, context) -> list:
        if self._describe_function:
            client = self.get_client(context)
            for resource in self.bar(context, resources, "describe"):
                if isinstance(resource, dict):
                    try:
                        self._describe(context, client, resource)
                    except ClientError as ex:
                        resource.update({"Describe": {"error": str(ex)}})
        return resources

    def _describe(self, context, client, resource):
        describe_function = getattr(client, self._describe_function)
        describe_identifier = self._get_describe_resource_identifier(context, resource)
        details = describe_function(**{self._describe_function_key: describe_identifier})
        resource.update({"Describe": details})


class MetricResourceInterface:

    def __init__(self):
        self._metric_namespace = ""
        self._metric_dimension_name = ""
        self._metric_dimension_resource_key = ""

    def _format_parameters(self,
                           statistic: str,
                           namespace: str, metric_name: str,
                           dimensions: dict = {},
                           period: int = 60*60, unit: str = "Count",
                           start_time: datetime = None, end_time: datetime = None) -> dict:
        # Set default parameter values
        start_time = start_time or datetime.today() - timedelta(days=90)
        end_time = end_time or datetime.today()
        return {
            "MetricDataQueries": [{
                "Id": f"cmq_{re.sub(r'[^a-zA-Z0-9]', '', metric_name)}",
                "MetricStat": {
                    "Metric": {
                        "Namespace": namespace,
                        "MetricName": metric_name,
                        "Dimensions": [
                            {"Name": k, "Value": v}
                            for k, v in dimensions.items()
                        ]
                    },
                    "Period": period,
                    "Stat": statistic,
                    "Unit": unit
                },
                "Label": unit,
                "ReturnData": True,
            }],
            "StartTime": start_time,
            "EndTime": end_time
        }

    def get_metric_data(self, results, context, **kwargs) -> list:
        """
        Retrieves metric data from AWS CloudWatch and processes it through the pipeline.

        Args:
            results (dict): The dictionary to store the results.
            context (dict): The context containing session information.
            **kwargs: Additional keyword arguments for the metric data query.

        Returns:
            list: List of metric data results.
        """
        client = self.get_client(context, "cloudwatch")
        dimensions = kwargs.pop("dimensions", {})
        dimensions[self._metric_dimension_name] = context[f"{self._desc}"][self._metric_dimension_resource_key]
        print(dimensions)

        parameters = self._format_parameters(
            namespace=self._metric_namespace,
            dimensions=dimensions,
            **kwargs
        )
        response = dimensions.copy()
        paginator = client.get_paginator("get_metric_data")

        for page in self.bar(context, paginator.paginate(**parameters), desc=f"metrics {dimensions[self._metric_dimension_name]}"):
            for metric in page["MetricDataResults"]:
                for key, value in metric.items():
                    if key in response and isinstance(value, list):
                        response[key].extend(value)
                    else:
                        response[key] = value
        account_list = results.setdefault(context["session_name"], [])
        account_list.append(response)
        return results

    def metric(self, **kwargs) -> dict:
        """
        Retrieves metric data from AWS CloudWatch and processes it through the pipeline.

        Args:
            **kwargs: Additional keyword arguments for the metric data query.

        Returns:
            dict: Dictionary of metric data results.
        """
        if not self._metric_namespace:
            exit(f"Metric namespace not defined for {self._service}")

        results: dict = {}
        self._perform_action(partial(self.get_metric_data, results, **kwargs))
        return results

    def plot(self, unit_factor=1, **kwargs) -> None:
        """
        Plots the metric data.

        Args:
            unit_factor (int): The factor to divide the metric values by.
            **kwargs: Additional keyword arguments for the metric data query.
        """
        resources = self.metric(**kwargs)

        plt.clf()
        for metrics in resources.values():
            for metric in metrics:
                timestamps = metric["Timestamps"]
                values = [value/unit_factor for value in metric["Values"]]
                label = metric.get(self._metric_dimension_name) or metric.get(self._metric_dimension_resource_key) or "Metric"
                plt.plot(timestamps, values, label=label)
        plt.title(f"{self._resource} {kwargs['statistic']} {kwargs['metric_name']}")
        plt.legend(loc='best')
        plt.show()


class AWSResource(TagResourceInterface, DescribeResourceInterface, MetricResourceInterface, AWSClientInterface, Resource):

    def __init__(self, parent=None):
        Resource.__init__(self, parent)
        AWSClientInterface.__init__(self)
        TagResourceInterface.__init__(self)
        DescribeResourceInterface.__init__(self)
        MetricResourceInterface.__init__(self)

    def bar(self, context, resources, desc: str = "", leave=True):
        if not self.enable_console():
            return resources
        desc = f"{context['session_name']: <20} {self._service} {desc}"
        if not getattr(resources, "__len__", None):
            resources = UnknownSizeIterator(resources)
            return InfiniteAtpbar(resources, name=desc, len_=len(resources))
        else:
            return Atpbar(resources, name=desc, len_=len(resources))

    def _get_pages(self, context) -> Any:
        return self.bar(context, super()._get_pages(context), desc=f"{self._desc} get_pages")

    def _list(self, results, context) -> None:
        results.append(context[f"{self._desc}"])

    def _dict(self, results, context) -> None:
        account_list = results.setdefault(context["session_name"], [])
        account_list.append(context.get(f"{self._desc}"))

