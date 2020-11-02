from dataclasses import field
from datetime import datetime
from typing import List, ClassVar, Dict

from marshmallow import Schema, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import NanoTimestampField, Resource, BanyanEnum


class TrustLevel(BanyanEnum):
    ALWAYS_ALLOW = "AlwaysAllow"
    ALWAYS_DENY = "AlwaysDeny"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


@dataclass
class TrustFactorDetailV2:
    class Meta:
        unknown = EXCLUDE

    factor_name: str = field(metadata={'data_key': 'FactorName'})
    factor_value: str = field(metadata={'data_key': 'FactorValue'})
    is_active: bool = field(metadata={'data_key': 'IsActive'})
    inactive_reason: str = field(metadata={'data_key': 'InactiveReason'})
    relative_contribution: int = field(metadata={'data_key': 'RelativeContribution'})
    recommendation: str = field(metadata={'data_key': 'Recommendation'})


@dataclass
class TrustFactorDetailsV2:
    class Meta:
        unknown = EXCLUDE

    details: Dict[str, TrustFactorDetailV2] = field(default_factory=dict, metadata={'data_key': 'Details'})


@dataclass
class TrustFactorV2:
    class Meta:
        unknown = EXCLUDE

    id: str = field(metadata={'data_key': 'Id'})
    name: str = field(metadata={'data_key': 'Name'})
    value: str = field(metadata={'data_key': 'Value'})
    resource_id: str = field(metadata={'data_key': 'ResourceId'})
    reporting_epoch: int = field(metadata={'data_key': 'ReportingEpoch'})
    source: str = field(metadata={'data_key': 'Source'})
    source_type: str = field(metadata={'data_key': 'SourceType'})
    factor_id: str = field(metadata={'data_key': 'FactorId'})
    is_ml_factor: bool = field(metadata={'data_key': 'IsMLFactor'})
    input_features: Dict[str, str] = field(metadata={'data_key': 'InputFeatures'})
    scoring_algo: str = field(metadata={'data_key': 'ScoringAlgo'})


@dataclass
class TrustFactorsV2(Resource):
    class Meta:
        unknown = EXCLUDE

    score_id: str = field(metadata={'data_key': 'Id'})
    algorithm_id: str = field(metadata={'data_key': 'AlgorithmId'})
    resource_id: str = field(metadata={'data_key': 'ResourceId'})
    score: int = field(metadata={'data_key': 'Score'})
    score_type: str = field(metadata={'data_key': 'ScoreType'})
    timestamp: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='Timestamp')})
    explanation: TrustFactorDetailsV2 = field(metadata={'data_key': 'Explanation'})
    created_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='CreatedAt')})
    updated_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='UpdatedAt')})
    factors_updated_at: datetime = field(metadata={'marshmallow_field':
                                                   NanoTimestampField(data_key='FactorsUpdatedAt')})
    active_factors: List[TrustFactorV2] = field(default_factory=list, metadata={'data_key': 'ActiveFactors'})
    inactive_factors: List[TrustFactorV2] = field(default_factory=list, metadata={'data_key': 'InactiveFactors'})
    Schema: ClassVar[Schema] = Schema

    @property
    def name(self) -> str:
        return self.score_id

    @property
    def id(self) -> str:
        return self.score_id
