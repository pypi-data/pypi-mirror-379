# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codeguru_reviewer import type_defs as bs_td


class CODEGURU_REVIEWERCaster:

    def associate_repository(
        self,
        res: "bs_td.AssociateRepositoryResponseTypeDef",
    ) -> "dc_td.AssociateRepositoryResponse":
        return dc_td.AssociateRepositoryResponse.make_one(res)

    def create_code_review(
        self,
        res: "bs_td.CreateCodeReviewResponseTypeDef",
    ) -> "dc_td.CreateCodeReviewResponse":
        return dc_td.CreateCodeReviewResponse.make_one(res)

    def describe_code_review(
        self,
        res: "bs_td.DescribeCodeReviewResponseTypeDef",
    ) -> "dc_td.DescribeCodeReviewResponse":
        return dc_td.DescribeCodeReviewResponse.make_one(res)

    def describe_recommendation_feedback(
        self,
        res: "bs_td.DescribeRecommendationFeedbackResponseTypeDef",
    ) -> "dc_td.DescribeRecommendationFeedbackResponse":
        return dc_td.DescribeRecommendationFeedbackResponse.make_one(res)

    def describe_repository_association(
        self,
        res: "bs_td.DescribeRepositoryAssociationResponseTypeDef",
    ) -> "dc_td.DescribeRepositoryAssociationResponse":
        return dc_td.DescribeRepositoryAssociationResponse.make_one(res)

    def disassociate_repository(
        self,
        res: "bs_td.DisassociateRepositoryResponseTypeDef",
    ) -> "dc_td.DisassociateRepositoryResponse":
        return dc_td.DisassociateRepositoryResponse.make_one(res)

    def list_code_reviews(
        self,
        res: "bs_td.ListCodeReviewsResponseTypeDef",
    ) -> "dc_td.ListCodeReviewsResponse":
        return dc_td.ListCodeReviewsResponse.make_one(res)

    def list_recommendation_feedback(
        self,
        res: "bs_td.ListRecommendationFeedbackResponseTypeDef",
    ) -> "dc_td.ListRecommendationFeedbackResponse":
        return dc_td.ListRecommendationFeedbackResponse.make_one(res)

    def list_recommendations(
        self,
        res: "bs_td.ListRecommendationsResponseTypeDef",
    ) -> "dc_td.ListRecommendationsResponse":
        return dc_td.ListRecommendationsResponse.make_one(res)

    def list_repository_associations(
        self,
        res: "bs_td.ListRepositoryAssociationsResponseTypeDef",
    ) -> "dc_td.ListRepositoryAssociationsResponse":
        return dc_td.ListRepositoryAssociationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)


codeguru_reviewer_caster = CODEGURU_REVIEWERCaster()
