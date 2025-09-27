# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_datasync import type_defs as bs_td


class DATASYNCCaster:

    def create_agent(
        self,
        res: "bs_td.CreateAgentResponseTypeDef",
    ) -> "dc_td.CreateAgentResponse":
        return dc_td.CreateAgentResponse.make_one(res)

    def create_location_azure_blob(
        self,
        res: "bs_td.CreateLocationAzureBlobResponseTypeDef",
    ) -> "dc_td.CreateLocationAzureBlobResponse":
        return dc_td.CreateLocationAzureBlobResponse.make_one(res)

    def create_location_efs(
        self,
        res: "bs_td.CreateLocationEfsResponseTypeDef",
    ) -> "dc_td.CreateLocationEfsResponse":
        return dc_td.CreateLocationEfsResponse.make_one(res)

    def create_location_fsx_lustre(
        self,
        res: "bs_td.CreateLocationFsxLustreResponseTypeDef",
    ) -> "dc_td.CreateLocationFsxLustreResponse":
        return dc_td.CreateLocationFsxLustreResponse.make_one(res)

    def create_location_fsx_ontap(
        self,
        res: "bs_td.CreateLocationFsxOntapResponseTypeDef",
    ) -> "dc_td.CreateLocationFsxOntapResponse":
        return dc_td.CreateLocationFsxOntapResponse.make_one(res)

    def create_location_fsx_open_zfs(
        self,
        res: "bs_td.CreateLocationFsxOpenZfsResponseTypeDef",
    ) -> "dc_td.CreateLocationFsxOpenZfsResponse":
        return dc_td.CreateLocationFsxOpenZfsResponse.make_one(res)

    def create_location_fsx_windows(
        self,
        res: "bs_td.CreateLocationFsxWindowsResponseTypeDef",
    ) -> "dc_td.CreateLocationFsxWindowsResponse":
        return dc_td.CreateLocationFsxWindowsResponse.make_one(res)

    def create_location_hdfs(
        self,
        res: "bs_td.CreateLocationHdfsResponseTypeDef",
    ) -> "dc_td.CreateLocationHdfsResponse":
        return dc_td.CreateLocationHdfsResponse.make_one(res)

    def create_location_nfs(
        self,
        res: "bs_td.CreateLocationNfsResponseTypeDef",
    ) -> "dc_td.CreateLocationNfsResponse":
        return dc_td.CreateLocationNfsResponse.make_one(res)

    def create_location_object_storage(
        self,
        res: "bs_td.CreateLocationObjectStorageResponseTypeDef",
    ) -> "dc_td.CreateLocationObjectStorageResponse":
        return dc_td.CreateLocationObjectStorageResponse.make_one(res)

    def create_location_s3(
        self,
        res: "bs_td.CreateLocationS3ResponseTypeDef",
    ) -> "dc_td.CreateLocationS3Response":
        return dc_td.CreateLocationS3Response.make_one(res)

    def create_location_smb(
        self,
        res: "bs_td.CreateLocationSmbResponseTypeDef",
    ) -> "dc_td.CreateLocationSmbResponse":
        return dc_td.CreateLocationSmbResponse.make_one(res)

    def create_task(
        self,
        res: "bs_td.CreateTaskResponseTypeDef",
    ) -> "dc_td.CreateTaskResponse":
        return dc_td.CreateTaskResponse.make_one(res)

    def describe_agent(
        self,
        res: "bs_td.DescribeAgentResponseTypeDef",
    ) -> "dc_td.DescribeAgentResponse":
        return dc_td.DescribeAgentResponse.make_one(res)

    def describe_location_azure_blob(
        self,
        res: "bs_td.DescribeLocationAzureBlobResponseTypeDef",
    ) -> "dc_td.DescribeLocationAzureBlobResponse":
        return dc_td.DescribeLocationAzureBlobResponse.make_one(res)

    def describe_location_efs(
        self,
        res: "bs_td.DescribeLocationEfsResponseTypeDef",
    ) -> "dc_td.DescribeLocationEfsResponse":
        return dc_td.DescribeLocationEfsResponse.make_one(res)

    def describe_location_fsx_lustre(
        self,
        res: "bs_td.DescribeLocationFsxLustreResponseTypeDef",
    ) -> "dc_td.DescribeLocationFsxLustreResponse":
        return dc_td.DescribeLocationFsxLustreResponse.make_one(res)

    def describe_location_fsx_ontap(
        self,
        res: "bs_td.DescribeLocationFsxOntapResponseTypeDef",
    ) -> "dc_td.DescribeLocationFsxOntapResponse":
        return dc_td.DescribeLocationFsxOntapResponse.make_one(res)

    def describe_location_fsx_open_zfs(
        self,
        res: "bs_td.DescribeLocationFsxOpenZfsResponseTypeDef",
    ) -> "dc_td.DescribeLocationFsxOpenZfsResponse":
        return dc_td.DescribeLocationFsxOpenZfsResponse.make_one(res)

    def describe_location_fsx_windows(
        self,
        res: "bs_td.DescribeLocationFsxWindowsResponseTypeDef",
    ) -> "dc_td.DescribeLocationFsxWindowsResponse":
        return dc_td.DescribeLocationFsxWindowsResponse.make_one(res)

    def describe_location_hdfs(
        self,
        res: "bs_td.DescribeLocationHdfsResponseTypeDef",
    ) -> "dc_td.DescribeLocationHdfsResponse":
        return dc_td.DescribeLocationHdfsResponse.make_one(res)

    def describe_location_nfs(
        self,
        res: "bs_td.DescribeLocationNfsResponseTypeDef",
    ) -> "dc_td.DescribeLocationNfsResponse":
        return dc_td.DescribeLocationNfsResponse.make_one(res)

    def describe_location_object_storage(
        self,
        res: "bs_td.DescribeLocationObjectStorageResponseTypeDef",
    ) -> "dc_td.DescribeLocationObjectStorageResponse":
        return dc_td.DescribeLocationObjectStorageResponse.make_one(res)

    def describe_location_s3(
        self,
        res: "bs_td.DescribeLocationS3ResponseTypeDef",
    ) -> "dc_td.DescribeLocationS3Response":
        return dc_td.DescribeLocationS3Response.make_one(res)

    def describe_location_smb(
        self,
        res: "bs_td.DescribeLocationSmbResponseTypeDef",
    ) -> "dc_td.DescribeLocationSmbResponse":
        return dc_td.DescribeLocationSmbResponse.make_one(res)

    def describe_task(
        self,
        res: "bs_td.DescribeTaskResponseTypeDef",
    ) -> "dc_td.DescribeTaskResponse":
        return dc_td.DescribeTaskResponse.make_one(res)

    def describe_task_execution(
        self,
        res: "bs_td.DescribeTaskExecutionResponseTypeDef",
    ) -> "dc_td.DescribeTaskExecutionResponse":
        return dc_td.DescribeTaskExecutionResponse.make_one(res)

    def list_agents(
        self,
        res: "bs_td.ListAgentsResponseTypeDef",
    ) -> "dc_td.ListAgentsResponse":
        return dc_td.ListAgentsResponse.make_one(res)

    def list_locations(
        self,
        res: "bs_td.ListLocationsResponseTypeDef",
    ) -> "dc_td.ListLocationsResponse":
        return dc_td.ListLocationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_task_executions(
        self,
        res: "bs_td.ListTaskExecutionsResponseTypeDef",
    ) -> "dc_td.ListTaskExecutionsResponse":
        return dc_td.ListTaskExecutionsResponse.make_one(res)

    def list_tasks(
        self,
        res: "bs_td.ListTasksResponseTypeDef",
    ) -> "dc_td.ListTasksResponse":
        return dc_td.ListTasksResponse.make_one(res)

    def start_task_execution(
        self,
        res: "bs_td.StartTaskExecutionResponseTypeDef",
    ) -> "dc_td.StartTaskExecutionResponse":
        return dc_td.StartTaskExecutionResponse.make_one(res)


datasync_caster = DATASYNCCaster()
