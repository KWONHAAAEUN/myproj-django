from django import forms
from news.models import Article

class Article(forms.ModelForm):
    class Meta:
        model=Article
        fiels="__all__"

        def clean_title(self):
            title=self.clean_title.get("title")
            if title:
                if len(title)<3:
                    raise forms.ValidationError("3글자 이상")
                return title