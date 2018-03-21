from django import forms
from djongo import models


class TestCase(models.Model):
    case_Name = models.CharField(max_length=100)
    objec = models.CharField(max_length=100)
    precon = models.CharField(max_length=100)
    step = models.ListField()
    check = models.ListField()
    prio = models.CharField(max_length=100)

    class Meta:
        abstract = True


class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ('case_Name', 'objec', 'precon', 'step', 'check', 'prio')


class Criteria(models.Model):
    cri_Name = models.CharField(max_length=100)
    cri_Given = models.ListField()
    cri_When = models.ListField()
    cri_Then = models.ListField()

    class Meta:
        abstract = True


class CriteriaForm(forms.ModelForm):
    class Meta:
        model = Criteria
        fields = ('cri_Name', 'cri_Given', 'cri_When', 'cri_Then')


class Story(models.Model):
    story_Name = models.CharField(max_length=100)
    as_Data = models.CharField(max_length=100)
    iWant = models.CharField(max_length=100)
    sothat = models.CharField(max_length=100)
    testcases = models.ArrayModelField(
        model_container=TestCase,
        model_form_class=TestCaseForm
    )
    criterias = models.ArrayModelField(
        model_container=Criteria,
        model_form_class=CriteriaForm
    )
    objects = models.DjongoManager()


# class TestCase(models.Model):
#     case_Name = models.CharField(max_length=100)
#     objec = models.CharField(max_length=100)
#     precon = models.CharField(max_length=100)
#     step = models.ListField()
#     check = models.ListField()
#     prio = models.CharField(max_length=100)
#     class Meta:
#         abstract = True

# class Criteria(models.Model):
#     cri_Name = models.CharField(max_length=100)
#     cri_Given = models.ListField()
#     cri_When = models.ListField()
#     cri_Then = models.ListField()
#     class Meta:
#         abstract = True

# class Story(models.Model):
#     idi = models.CharField(max_length=100)
#     story_Name = models.CharField(max_length=100)
#     as_Data = models.CharField(max_length=100)
#     iWant = models.CharField(max_length=100)
#     sothat = models.CharField(max_length=100)
#     tags = models.ListField()
#     testcases = models.ArrayModelField(TestCase, forms.ModelForm)
#     criterias = models.ArrayModelField(Criteria, forms.ModelForm)
