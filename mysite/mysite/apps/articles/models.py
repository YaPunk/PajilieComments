from django.db import models

class Article(models.Model):
	title = models.CharField("article title", max_length = 100)
	text = models.TextField("article text")
	author_name = models.CharField("article author name", max_length = 50)
	pub_date = models.DateTimeField("article publication date")
	
	def __str__(self):
		return self.title + ' | ' + self.text	

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'	

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	text = models.TextField("comment text")
	author_name = models.CharField("comment author name", max_length = 50)
	pub_date = models.DateTimeField("comment publication date")

	def __str__(self):
		return self.text

	
	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
