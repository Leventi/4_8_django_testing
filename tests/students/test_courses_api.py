import pytest as pytest
from django.urls import reverse


@pytest.mark.django_db
def test_detail_course(client, course_factory):
    course_factory(_quantity=10)
    url = reverse("courses-detail", kwargs={'pk': 2})
    response = client().get(url)

    assert response.status_code == 200
    assert response.data['id'] == 2


@pytest.mark.django_db
def test_list_course(client, course_factory):
    course_factory(_quantity=10)
    url = reverse("courses-list")
    response = client().get(url)

    assert response.status_code == 200
    assert len(response.data) == 10


@pytest.mark.django_db
def test_id_filter_course(client, course_factory):
    course_factory(_quantity=10)
    url = reverse("courses-list")
    response = client().get(url, {'id': 2})

    assert response.status_code == 200


@pytest.mark.django_db
def test_name_filter_course(client, course_factory):
    dammy_data = course_factory(_quantity=10)
    dammy_data_name = dammy_data[0].name
    url = reverse("courses-list")
    response = client().get(url, {'name': dammy_data_name})

    assert response.status_code == 200
    assert response.data[0]['name'] == dammy_data_name

@pytest.mark.django_db
def test_create_course(client, course_data):
    url = reverse("courses-list")
    response = client().post(url, course_data)

    assert response.status_code == 201

@pytest.mark.django_db
def test_update_course(client, course_factory, course_data):
    course_factory(_quantity=10)
    url = reverse("courses-detail", kwargs={'pk': 2})
    response = client().patch(url, course_data)

    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course_factory(_quantity=10)
    url = reverse("courses-detail", kwargs={'pk': 2})
    response = client().delete(url)

    assert response.status_code == 204



# @pytest.mark.django_db
# def test_max_students_course(client, max_students, course_data, student_factory):
#     student_factory(_quantity=10)
#     url = reverse("courses-list")
#     response = client().post(url, course_data)
#
#     assert response.status_code == 201



