from django import forms

def check_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError('data is not valid')
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.CharField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)


    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        a=self.cleaned_data['age']
        if e!=r or a<18:
            raise forms.ValidationError('data is not valid')
        
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']

        if len(bot)>0:
            raise forms.ValidationError('you bloody bot')
