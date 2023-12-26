from tests import *

test_courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
                    "Frontend-разработчик с нуля"]

test_durations = [14, 20, 12, 20]

test_mentors = [
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков", "Роман Гордиенко"],
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]


class TestTop:

    def test_top3_stability(self):
        result1 = get_top3(sample(m, len(m)) for m in test_mentors)
        result2 = get_top3(test_mentors)
        assert result1 == result2, ErrorMessages.INSTABILITY.value

    def test_top3_answer(self):
        expected = [('Александр', 10), ('Евгений', 5), ('Максим', 4)]
        result = get_top3(test_mentors)
        assert result == expected, ErrorMessages.WRONG_ANSWER.value


class TestOrder:

    @pytest.mark.parametrize("courses, durations", (
            [["python", "java", "sql", "JavaScript"], [18, 24, 10, 11]],
            [test_courses, test_durations],
            [sample(test_courses, len(test_courses)), sample(test_durations, len(test_durations))]
            )
    )
    def test_order_answer(self, courses, durations):
        res = order_by_duration(courses, durations)
        for i, item in enumerate(res[1:], start=1):
            assert item["duration"] >= res[i-1]["duration"], ErrorMessages.WRONG_ORDER.value

    @pytest.mark.parametrize("courses, durations", (
            [["python", "java", "sql", "JavaScript"], [18, 24, 10, 11]],
            [test_courses, test_durations]
        )
    )
    def test_order_coherence(self, courses, durations):
        res = order_by_duration(courses, durations)
        for item in res:
            index_course = courses.index(item["title"])
            assert durations[index_course] == item["duration"], ErrorMessages.DEFORM_VALUE.value


class TestUnique:

    @pytest.mark.parametrize("mentors", (
            test_mentors,
            sample(test_mentors, len(test_mentors)),
            [sample(m, len(m)) for m in test_mentors]
        )
    )
    def test_uniq(self, mentors):
        result = get_unique_names(mentors)
        assert len(result) == len(set(result)), ErrorMessages.NON_UNIQUE.value


    @pytest.mark.parametrize("mentors", (
            test_mentors,
            sample(test_mentors, len(test_mentors)),
            [sample(m, len(m)) for m in test_mentors]
    )
                             )
    def test_value(self, mentors):
        result = get_unique_names(mentors)
        all_names = [mentor.split()[0] for cours_mentors in mentors for mentor in cours_mentors]
        assert all(name in all_names for name in result), ErrorMessages.DEFORM_VALUE.value