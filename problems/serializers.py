from rest_framework import serializers
from .models import Problem, File

class FileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ['id', 'file', 'file_url', 'uploaded_at']

    def get_file_url(self, obj):
        return obj.file.url

class ProblemSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True)
    files_upload = serializers.ListField(
        child=serializers.FileField(write_only=True), write_only=True, required=False
    )

    class Meta:
        model = Problem
        fields = ['id', 'title', 'subject', 'description', 'author', 'created_at', 'updated_at', 'approved', 'difficulty', 'files', 'files_upload', 'answer']

    def create(self, validated_data):
        files_data = validated_data.pop('files_upload', [])
        problem = Problem.objects.create(**validated_data)
        for file_data in files_data:
            file_instance = File.objects.create(file=file_data)
            problem.files.add(file_instance)
        return problem
