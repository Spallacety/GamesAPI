from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = ('id', 'created', 'name', 'release_date', 'game_category', 'played')

  def is_empty(self, field):
    if field is None or field == "":
      raise serializers.ValidationError("Empty field!")
    return field

  def verify_name(self, name):
    if name in list(map(lambda game: game.name, Game.objects.filter(name=name).exclude(id=self.initial_data['id']))):
      raise serializers.ValidationError("A game with this name already exists!")

  def validate_name(self, name):
    self.verify_name(name)
    return self.is_empty(field=name)

  def validate_release_date(self, release_date):
    return self.is_empty(field=release_date)

  def validate_game_category(self, game_category):
    return self.is_empty(field=game_category)