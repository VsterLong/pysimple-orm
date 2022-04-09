from typing import List
import orm.sql_manage as SqlAgent
from models.entity import GroupByTotal, TbFamilyPerson


def distinct():
    sql = """
    select person_num as group_key, count(1) as total from tb_family_person
    where person_num is not null and length(trim(person_num)) != 0 
    group by person_num, village having count(1) > 1
    """
    fas: List[GroupByTotal] = SqlAgent.do_select_all(
        sql=sql, class_name=GroupByTotal)
    question_fas: List[TbFamilyPerson] = SqlAgent.do_select_all(
        "select * from tb_family_person where person_num in %s", class_name=TbFamilyPerson, param=([item.group_key for item in fas],))
    print("去重前：{}条，去重后：{}条。".format(len(question_fas), len(set(question_fas))))
    for item in question_fas:
        print(item.id_card, item.person_name)


if __name__ == "__main__":
    distinct()
