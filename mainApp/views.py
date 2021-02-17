from django.shortcuts import render
from .models import Owner, Education, Experience, Volunteering, Tool, SoftSkill, MainSkill, Language,\
    ProgrammingSkill, Testimonial, Project


def home(request):
    owner = Owner.objects.first()
    if owner:
        owner.profile_image = str(owner.profile_image).split('/', 1)[1]
        owner.background_image = str(owner.background_image).split('/', 1)[1]
        owner.favicon = str(owner.favicon).split('/', 1)[1]
    educations = Education.objects.order_by('-year_start')
    experiences = Experience.objects.order_by('-year_start', '-month_start')
    volunteerings = Volunteering.objects.order_by('-year_start', '-month_start')
    tools = Tool.objects.all()
    tools = zip(tools, range(0, Tool.objects.count() * 100, 100))
    soft_skills = SoftSkill.objects.all()
    if soft_skills:
        for soft_skill in soft_skills:
            soft_skill.logo = str(soft_skill.logo).split('/', 1)[1]

    main_skills = MainSkill.objects.all()
    if main_skills:
        for main_skill in main_skills:
            main_skill.logo = str(main_skill.logo).split('/', 1)[1]

    languages = Language.objects.all()
    programming_skills = ProgrammingSkill.objects.all()
    if programming_skills:
        for programming_skill in programming_skills:
            programming_skill.logo = str(programming_skill.logo).split('/', 1)[1]

    testimonials = Testimonial.objects.all()
    if testimonials:
        for testimonial in testimonials:
            testimonial.image = str(testimonial.image).split('/', 1)[1]

    projects = Project.objects.all()
    return render(request, 'home.html', {'owner': owner, 'educations': educations, 'experiences': experiences,
                                         'volunteerings': volunteerings, 'tools': tools, 'soft_skills': soft_skills,
                                         'main_skills': main_skills, 'languages': languages,
                                         'programming_skills': programming_skills, 'testimonials': testimonials,
                                         'projects': projects})
