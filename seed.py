from jobs.models import Job
from applications.models import Application
from freelancer.models import Freelancer
from django.contrib.auth.models import User


def create_freelancers():
    freelancers_data = [
        {"username": "freelancer1", "password": "pass1",
            "email": "freelancer1@example.com", "skills": "Python, Django"},
        {"username": "freelancer2", "password": "pass2",
            "email": "freelancer2@example.com", "skills": "JavaScript, React"},
        {"username": "freelancer3", "password": "pass3",
            "email": "freelancer3@example.com", "skills": "Java, Spring"},
        {"username": "freelancer4", "password": "pass4",
            "email": "freelancer4@example.com", "skills": "C++, Qt"},
        {"username": "freelancer5", "password": "pass5",
            "email": "freelancer5@example.com", "skills": "Ruby, Rails"},
    ]
    for freelancer_data in freelancers_data:
        user = User.objects.create_user(
            username=freelancer_data["username"],
            password=freelancer_data["password"],
            email=freelancer_data["email"]
        )
        Freelancer.objects.create(user=user, skills=freelancer_data["skills"])


def create_jobs():
    jobs = [
        {"title": "Job 1", "description": "Description 1",
            "required_skills": "Skill 1, Skill 2"},
        {"title": "Job 2", "description": "Description 2",
            "required_skills": "Skill 3, Skill 4"},
        {"title": "Job 3", "description": "Description 3",
            "required_skills": "Skill 5, Skill 6"},
        {"title": "Job 4", "description": "Description 4",
            "required_skills": "Skill 7, Skill 8"},
        {"title": "Job 5", "description": "Description 5",
            "required_skills": "Skill 9, Skill 10"},
    ]
    for job_data in jobs:
        Job.objects.create(**job_data)


def create_applications():
    freelancers = Freelancer.objects.all()
    jobs = Job.objects.all()
    for freelancer in freelancers:
        for job in jobs[:3]:  # Create 3 applications for each freelancer
            Application.objects.create(
                job=job,
                freelancer=freelancer,
                status="pending"
            )


if __name__ == "__main__":
    create_freelancers()
    create_jobs()
    create_applications()
    print("Seeding completed.")
