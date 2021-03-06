import datetime
import json
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.affect_meta_attr import AffectMetaAttr
from ..models.affect_resolution_enum import AffectResolutionEnum
from ..models.affect_type_enum import AffectTypeEnum
from ..models.affectedness_enum import AffectednessEnum
from ..models.blank_enum import BlankEnum
from ..models.impact_enum import ImpactEnum
from ..models.tracker import Tracker
from ..types import UNSET, Unset

T = TypeVar("T", bound="Affect")


@attr.s(auto_attribs=True)
class Affect:
    """Affect serializer"""

    uuid: str
    ps_module: str
    ps_component: str
    trackers: List[Tracker]
    meta_attr: AffectMetaAttr
    delegated_resolution: str
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    flaw: Optional[str]
    type: Union[Unset, AffectTypeEnum] = UNSET
    affectedness: Union[AffectednessEnum, BlankEnum, Unset] = UNSET
    resolution: Union[AffectResolutionEnum, BlankEnum, Unset] = UNSET
    impact: Union[BlankEnum, ImpactEnum, Unset] = UNSET
    cvss2: Union[Unset, str] = UNSET
    cvss2_score: Union[Unset, None, float] = UNSET
    cvss3: Union[Unset, str] = UNSET
    cvss3_score: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        ps_module = self.ps_module
        ps_component = self.ps_component
        trackers: List[Dict[str, Any]] = UNSET
        if not isinstance(self.trackers, Unset):
            trackers = []
            for trackers_item_data in self.trackers:
                trackers_item: Dict[str, Any] = UNSET
                if not isinstance(trackers_item_data, Unset):
                    trackers_item = trackers_item_data.to_dict()

                trackers.append(trackers_item)

        meta_attr: Dict[str, Any] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        delegated_resolution = self.delegated_resolution
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        flaw = self.flaw
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):

            type = AffectTypeEnum(self.type).value

        affectedness: Union[Unset, str]
        if isinstance(self.affectedness, Unset):
            affectedness = UNSET
        elif isinstance(self.affectedness, AffectednessEnum):
            affectedness = UNSET
            if not isinstance(self.affectedness, Unset):

                affectedness = AffectednessEnum(self.affectedness).value

        else:
            affectedness = UNSET
            if not isinstance(self.affectedness, Unset):

                affectedness = BlankEnum(self.affectedness).value

        resolution: Union[Unset, str]
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif isinstance(self.resolution, AffectResolutionEnum):
            resolution = UNSET
            if not isinstance(self.resolution, Unset):

                resolution = AffectResolutionEnum(self.resolution).value

        else:
            resolution = UNSET
            if not isinstance(self.resolution, Unset):

                resolution = BlankEnum(self.resolution).value

        impact: Union[Unset, str]
        if isinstance(self.impact, Unset):
            impact = UNSET
        elif isinstance(self.impact, ImpactEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):

                impact = ImpactEnum(self.impact).value

        else:
            impact = UNSET
            if not isinstance(self.impact, Unset):

                impact = BlankEnum(self.impact).value

        cvss2 = self.cvss2
        cvss2_score = self.cvss2_score
        cvss3 = self.cvss3
        cvss3_score = self.cvss3_score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if ps_module is not UNSET:
            field_dict["ps_module"] = ps_module
        if ps_component is not UNSET:
            field_dict["ps_component"] = ps_component
        if trackers is not UNSET:
            field_dict["trackers"] = trackers
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr
        if delegated_resolution is not UNSET:
            field_dict["delegated_resolution"] = delegated_resolution
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if updated_dt is not UNSET:
            field_dict["updated_dt"] = updated_dt
        if flaw is not UNSET:
            field_dict["flaw"] = flaw
        if type is not UNSET:
            field_dict["type"] = type
        if affectedness is not UNSET:
            field_dict["affectedness"] = affectedness
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if impact is not UNSET:
            field_dict["impact"] = impact
        if cvss2 is not UNSET:
            field_dict["cvss2"] = cvss2
        if cvss2_score is not UNSET:
            field_dict["cvss2_score"] = cvss2_score
        if cvss3 is not UNSET:
            field_dict["cvss3"] = cvss3
        if cvss3_score is not UNSET:
            field_dict["cvss3_score"] = cvss3_score

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        ps_module = self.ps_module if self.ps_module is UNSET else (None, str(self.ps_module), "text/plain")
        ps_component = self.ps_component if self.ps_component is UNSET else (None, str(self.ps_component), "text/plain")
        trackers: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.trackers, Unset):
            _temp_trackers = []
            for trackers_item_data in self.trackers:
                trackers_item: Dict[str, Any] = UNSET
                if not isinstance(trackers_item_data, Unset):
                    trackers_item = trackers_item_data.to_dict()

                _temp_trackers.append(trackers_item)
            trackers = (None, json.dumps(_temp_trackers), "application/json")

        meta_attr: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = (None, json.dumps(self.meta_attr.to_dict()), "application/json")

        delegated_resolution = (
            self.delegated_resolution
            if self.delegated_resolution is UNSET
            else (None, str(self.delegated_resolution), "text/plain")
        )
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        flaw = self.flaw if self.flaw is UNSET else (None, str(self.flaw), "text/plain")
        type: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.type, Unset):

            type = AffectTypeEnum(self.type).value

        affectedness: Union[Unset, str]
        if isinstance(self.affectedness, Unset):
            affectedness = UNSET
        elif isinstance(self.affectedness, AffectednessEnum):
            affectedness = UNSET
            if not isinstance(self.affectedness, Unset):

                affectedness = AffectednessEnum(self.affectedness).value

        else:
            affectedness = UNSET
            if not isinstance(self.affectedness, Unset):

                affectedness = BlankEnum(self.affectedness).value

        resolution: Union[Unset, str]
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif isinstance(self.resolution, AffectResolutionEnum):
            resolution = UNSET
            if not isinstance(self.resolution, Unset):

                resolution = AffectResolutionEnum(self.resolution).value

        else:
            resolution = UNSET
            if not isinstance(self.resolution, Unset):

                resolution = BlankEnum(self.resolution).value

        impact: Union[Unset, str]
        if isinstance(self.impact, Unset):
            impact = UNSET
        elif isinstance(self.impact, ImpactEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):

                impact = ImpactEnum(self.impact).value

        else:
            impact = UNSET
            if not isinstance(self.impact, Unset):

                impact = BlankEnum(self.impact).value

        cvss2 = self.cvss2 if self.cvss2 is UNSET else (None, str(self.cvss2), "text/plain")
        cvss2_score = self.cvss2_score if self.cvss2_score is UNSET else (None, str(self.cvss2_score), "text/plain")
        cvss3 = self.cvss3 if self.cvss3 is UNSET else (None, str(self.cvss3), "text/plain")
        cvss3_score = self.cvss3_score if self.cvss3_score is UNSET else (None, str(self.cvss3_score), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if ps_module is not UNSET:
            field_dict["ps_module"] = ps_module
        if ps_component is not UNSET:
            field_dict["ps_component"] = ps_component
        if trackers is not UNSET:
            field_dict["trackers"] = trackers
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr
        if delegated_resolution is not UNSET:
            field_dict["delegated_resolution"] = delegated_resolution
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if updated_dt is not UNSET:
            field_dict["updated_dt"] = updated_dt
        if flaw is not UNSET:
            field_dict["flaw"] = flaw
        if type is not UNSET:
            field_dict["type"] = type
        if affectedness is not UNSET:
            field_dict["affectedness"] = affectedness
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if impact is not UNSET:
            field_dict["impact"] = impact
        if cvss2 is not UNSET:
            field_dict["cvss2"] = cvss2
        if cvss2_score is not UNSET:
            field_dict["cvss2_score"] = cvss2_score
        if cvss3 is not UNSET:
            field_dict["cvss3"] = cvss3
        if cvss3_score is not UNSET:
            field_dict["cvss3_score"] = cvss3_score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        ps_module = d.pop("ps_module", UNSET)

        ps_component = d.pop("ps_component", UNSET)

        trackers = []
        _trackers = d.pop("trackers", UNSET)
        if _trackers is UNSET:
            trackers = UNSET
        else:
            for trackers_item_data in _trackers or []:
                _trackers_item = trackers_item_data
                trackers_item: Tracker
                if isinstance(_trackers_item, Unset):
                    trackers_item = UNSET
                else:
                    trackers_item = Tracker.from_dict(_trackers_item)

                trackers.append(trackers_item)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: AffectMetaAttr
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = AffectMetaAttr.from_dict(_meta_attr)

        delegated_resolution = d.pop("delegated_resolution", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        flaw = d.pop("flaw", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AffectTypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AffectTypeEnum(_type)

        def _parse_affectedness(data: object) -> Union[AffectednessEnum, BlankEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _affectedness_type_0 = data
                affectedness_type_0: Union[Unset, AffectednessEnum]
                if isinstance(_affectedness_type_0, Unset):
                    affectedness_type_0 = UNSET
                else:
                    affectedness_type_0 = AffectednessEnum(_affectedness_type_0)

                return affectedness_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _affectedness_type_1 = data
            affectedness_type_1: Union[Unset, BlankEnum]
            if isinstance(_affectedness_type_1, Unset):
                affectedness_type_1 = UNSET
            else:
                affectedness_type_1 = BlankEnum(_affectedness_type_1)

            return affectedness_type_1

        affectedness = _parse_affectedness(d.pop("affectedness", UNSET))

        def _parse_resolution(data: object) -> Union[AffectResolutionEnum, BlankEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _resolution_type_0 = data
                resolution_type_0: Union[Unset, AffectResolutionEnum]
                if isinstance(_resolution_type_0, Unset):
                    resolution_type_0 = UNSET
                else:
                    resolution_type_0 = AffectResolutionEnum(_resolution_type_0)

                return resolution_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _resolution_type_1 = data
            resolution_type_1: Union[Unset, BlankEnum]
            if isinstance(_resolution_type_1, Unset):
                resolution_type_1 = UNSET
            else:
                resolution_type_1 = BlankEnum(_resolution_type_1)

            return resolution_type_1

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_impact(data: object) -> Union[BlankEnum, ImpactEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _impact_type_0 = data
                impact_type_0: Union[Unset, ImpactEnum]
                if isinstance(_impact_type_0, Unset):
                    impact_type_0 = UNSET
                else:
                    impact_type_0 = ImpactEnum(_impact_type_0)

                return impact_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _impact_type_1 = data
            impact_type_1: Union[Unset, BlankEnum]
            if isinstance(_impact_type_1, Unset):
                impact_type_1 = UNSET
            else:
                impact_type_1 = BlankEnum(_impact_type_1)

            return impact_type_1

        impact = _parse_impact(d.pop("impact", UNSET))

        cvss2 = d.pop("cvss2", UNSET)

        cvss2_score = d.pop("cvss2_score", UNSET)

        cvss3 = d.pop("cvss3", UNSET)

        cvss3_score = d.pop("cvss3_score", UNSET)

        affect = cls(
            uuid=uuid,
            ps_module=ps_module,
            ps_component=ps_component,
            trackers=trackers,
            meta_attr=meta_attr,
            delegated_resolution=delegated_resolution,
            created_dt=created_dt,
            updated_dt=updated_dt,
            flaw=flaw,
            type=type,
            affectedness=affectedness,
            resolution=resolution,
            impact=impact,
            cvss2=cvss2,
            cvss2_score=cvss2_score,
            cvss3=cvss3,
            cvss3_score=cvss3_score,
        )

        affect.additional_properties = d
        return affect

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
