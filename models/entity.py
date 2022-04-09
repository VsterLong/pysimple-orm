from uuid import UUID


class TbFamilyPerson(object):
    def __init__(self) -> None:
        self.id = ""
        self.person_num = ""
        self.id_card = ""
        self.household_id_card = ""
        self.household_name = ""
        self.will1 = ""
        self.village = ""
        self.person_name = ""

    def __eq__(self, other) -> bool:
        if self.person_num == other.person_num:
            return True

        return False

    def __hash__(self) -> int:
        return hash(self.person_num)


class TbPersonnelManage:
    id: UUID
    create_by: str
    create_time: str
    update_by: str
    update_time: str
    sys_org_code: str
    name: str
    gender: str
    nation: str
    id_card: str
    birth: str
    education: str
    political_status: str
    healthy_status: str
    disability_cert: str
    personnel_status: str
    has_moved_in: str
    blg_reloc_obj: str
    blg_entire_village_reloc_obj: str
    move_out_place_id: str
    move_in_place_id: str
    residential_area: str
    move_in_place_name: str
    move_out_village: str
    household_relation: str
    register_number: str
    residential_area_id: str
    out_poverty_status: str
    extremely_poor_status: str
    change_date: str
    village: str
    village_id: str
    valid_status: str
    integrity_status: int
    household_name: str
    household_id_card: str

    def __init__(self) -> None:
        self.id = None
        self.create_by = ""
        self.create_time = ""
        self.update_by = ""
        self.update_time = ""
        self.sys_org_code = ""
        self.name = ""
        self.gender = ""
        self.nation = ""
        self.id_card = ""
        self.birth = ""
        self.education = ""
        self.political_status = ""
        self.healthy_status = ""
        self.disability_cert = ""
        self.personnel_status = ""
        self.has_moved_in = ""
        self.blg_reloc_obj = ""
        self.blg_entire_village_reloc_obj = ""
        self.move_out_place_id = ""
        self.move_in_place_id = ""
        self.residential_area = ""
        self.move_in_place_name = ""
        self.move_out_village = ""
        self.household_relation = ""
        self.register_number = ""
        self.residential_area_id = ""
        self.out_poverty_status = ""
        self.extremely_poor_status = ""
        self.change_date = ""
        self.village = ""
        self.village_id = ""
        self.valid_status = ""
        self.integrity_status = ""
        self.household_name = ""
        self.household_id_card = ""


class TbLaborForceSituation:
    def __init__(self) -> None:
        self.id = ""
        self.personnel_id = ""
        self.personnel_name = ""
        self.village = ""
        self.village_id = ""


class GroupByTotal():
    def __init__(self) -> None:
        self.group_key = ""
        self.total = 0
