from apps.certificate.certificate import CertificateGenerator, CertificateGenerator2, CertificateGenerator3
import os

from datetime import datetime

def first_certificate(certificate):
    file_path =f"media/first_certificate/{certificate.student.login}{certificate.id}.pdf"
    if not os.path.exists(file_path):
        generator = CertificateGenerator(
            file_path=file_path,
            student_name=certificate.student.username,
            group_name=certificate.student.group_name,
            direction_number="0000000",
            direction_name=certificate.student.direction_name,
            study_type=certificate.student.study_form,
            level=certificate.student.study_degree,
            faculty_name=certificate.student.faculty_name,
            issue_date=certificate.issue_date,
            course_num=certificate.student.course_num,
            certificate_num=certificate.certificate_num,
            dean_signature_path='apps/certificate/test_images/signature.png',
            secretary_signature_path='apps/certificate/test_images/signature2.png',
            seal_image_path='apps/certificate/test_images/seal.jpg',
            ministry="МИНИСТЕРСТВО ОБРАЗОВАНИЯ И НАУКИ КЫРГЫЗСКОЙ РЕСПУБЛИКИ",
            university_name=certificate.student.university_name
        )
        generator.generate_certificate()
    return file_path


def second_certificate(certificate):
    file_path =f"media/second_certificate/{certificate.student.login}{certificate.id}.pdf"
    if not os.path.exists(file_path):
        current_year = datetime.now().year
        semesters_data = [
            {"name": "осенний семестр", "start": f"01.09.{current_year}", "end": f"31.12.{current_year}"},
            {"name": "весенний семестр", "start": f"01.02.{current_year + 1}", "end": f"31.05.{current_year + 1}"},
            {"name": "каникулярный семестр", "start": f"01.06.{current_year + 1}", "end": f"31.08.{current_year + 1}"}
        ]
        generator2 = CertificateGenerator2(
            file_path=file_path,
            student_name=certificate.student.username,
            date_of_birth=certificate.student.date_of_birth,
            course_num=certificate.student.course_num,
            group_name=certificate.student.group_name,
            faculty_name=certificate.student.faculty_name,
            study_form=certificate.student.study_form,
            period_start=certificate.student.period_start,
            period_end=certificate.student.period_end,
            normative_duration=certificate.student.normative_duration,
            to_the_authority=certificate.embassy,
            certificate_num=certificate.certificate_num, 
            executor_name=certificate.executor_name,
            execution_date=certificate.issue_date,

            qr_code_data=f"http://127.0.0.1:8000/media/second_certificate/{certificate.student.email}{certificate.id}.pdf",
            # TODO: QR code should show some information automatically
            # without having to enter it as a parameter, replace it later
            # when info is gathered from the university.

            project_authority_name=certificate.project_authority_name,
            project_authority_role=certificate.project_authority_role,
            project_authority_sign_path='apps/certificate/test_images/signature2.png',
            ministry="МИНИСТЕРСТВО ОБРАЗОВАНИЯ И НАУКИ КЫРГЫЗСКОЙ РЕСПУБЛИКИ",
            university_name=certificate.student.university_name,
            seal_image_path='apps/certificate/test_images/seal.jpg',
            semesters=semesters_data
        )
        generator2.generate_certificate()
    return file_path


def third_certificate(certificate):
    file_path =f"media/third_certificate/{certificate.student.login}{certificate.id}.pdf"
    if not os.path.exists(file_path):
        generator3 = CertificateGenerator3(
            file_path=file_path,
            ministry="МИНИСТЕРСТВО ОБРАЗОВАНИЯ И НАУКИ КЫРГЫЗСКОЙ РЕСПУБЛИКИ",
            university=certificate.student.university_name,
            university_address="ул. Фрунзе - 547",
            full_name=certificate.student.username,
            birthday=certificate.student.date_of_birth,
            year_of_admission=certificate.student.period_start.year,
            faculty_name=certificate.student.faculty_name,
            date_of_admission_dd_mm_yyyy=certificate.student.period_start,
            order_number="123",
            course_num=certificate.student.course_num,
            type_of_study_ru=certificate.student.study_form,
            license="AL317",
            year_of_license="2004",
            year_of_finish_yyyy_mm=certificate.student.period_end,
            district=certificate.district,
            seal_image_path='apps/certificate/test_images/seal.jpg',
            signature1_path='apps/certificate/test_images/signature.png',
            signature2_path='apps/certificate/test_images/signature2.png',
            signature3_path='apps/certificate/test_images/signature3.png',
        )
        generator3.generate_certificate()
    return file_path