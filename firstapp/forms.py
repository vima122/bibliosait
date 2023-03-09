from django import forms
class loginbook(forms.Form):
    photo = forms.ImageField(label="",widget=forms.FileInput(attrs={"class":"book"}))
    name = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"vvod","placeholder":"Название"}))
    avtor = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"vvod","placeholder":"Автор"}))
    janr = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"vvod","placeholder":"Жанр"}))
    star = forms.IntegerField(label="",widget=forms.NumberInput(attrs={"class":"vvod","placeholder":"Оценка"}))
    place = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"vvod","placeholder":"Местоположение"}))
    aboutbook = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"vvod about","placeholder":"Краткое описание"}))
    
class loginuser(forms.Form):
    login = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"login"}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"class":"pass"}))
class search(forms.Form):
    search = forms.CharField(label="",widget=forms.TextInput(attrs={"id":"search-text"}))
    choice = forms.ChoiceField(choices=((1, "По авторам"), (2, "По названию"), (3, "По жанру")))
