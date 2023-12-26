def get_top3(mentors):
    all_mentors = []
    for m in mentors:
        all_mentors.extend(m)
    all_names_list = [m.split()[0] for m in all_mentors]
    unique_names = set(all_names_list)
    popular = []
    for name in unique_names:
        popular.append((name, all_names_list.count(name)))
    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = popular[:3]
    return top_3


def order_by_duration(courses, durations):
    courses_list = []
    for course, duration in zip(courses, durations):
        courses_list.append({"title": course, "duration": duration})
    courses_list.sort(key=lambda x: x['duration'])
    return courses_list


def get_unique_names(mentors):
    print(mentors)
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = [mentor.split()[0] for mentor in all_list]
    unique_names = set(all_names_list)
    return sorted(unique_names)


