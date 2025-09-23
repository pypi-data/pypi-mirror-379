from django.contrib.auth import get_user_model
from rest_framework import serializers

from huscy.project_design import models, services

User = get_user_model()


class DataAcquisitionMethodSerializer(serializers.ModelSerializer):
    location = serializers.CharField(required=False)
    setup_time = serializers.DurationField(required=False)
    teardown_time = serializers.DurationField(required=False)

    class Meta:
        model = models.DataAcquisitionMethod
        fields = (
            'id',
            'duration',
            'location',
            'order',
            'session',
            'setup_time',
            'stimulus',
            'teardown_time',
            'type',
        )
        read_only_fields = 'id', 'order', 'session'

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method == 'PUT':
            fields['type'].read_only = True
        return fields

    def create(self, validated_data):
        return services.create_data_acquisition_method(**validated_data)

    def update(self, data_acquisition_method, validated_data):
        return services.update_data_acquisition_method(data_acquisition_method, **validated_data)


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'first_name',
            'full_name',
            'last_name',
            'username',
        )

    def get_full_name(self, user):
        return user.get_full_name()


class SessionSerializer(serializers.ModelSerializer):
    contacts = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(),
                                                  write_only=True)
    data_acquisition_methods = DataAcquisitionMethodSerializer(many=True, read_only=True)
    duration = serializers.SerializerMethodField()

    class Meta:
        model = models.Session
        fields = (
            'id',
            'contacts',
            'data_acquisition_methods',
            'duration',
            'experiment',
            'order',
            'title',
        )
        read_only_fields = 'id', 'experiment', 'order'

    def update(self, session, validated_data):
        return services.update_session(session, **validated_data)

    def get_duration(self, session):
        return "{:0>8}".format(str(session.duration))

    def to_representation(self, session):
        result = super().to_representation(session)
        result['contacts'] = UserSerializer(session.contacts, many=True).data
        return result


class CreateSessionSerializer(serializers.ModelSerializer):
    contacts = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(),
                                                  write_only=True)
    data_acquisition_methods = DataAcquisitionMethodSerializer(many=True, required=False)
    title = serializers.CharField(required=False)

    class Meta:
        model = models.Session
        fields = (
            'contacts',
            'data_acquisition_methods',
            'title',
        )

    def create(self, validated_data):
        return services.create_session(**validated_data)

    def to_representation(self, session):
        return SessionSerializer(instance=session).data


class ExperimentSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Experiment
        fields = (
            'id',
            'description',
            'order',
            'project',
            'sessions',
            'title',
        )
        read_only_fields = 'id', 'project'

    def update(self, experiment, validated_data):
        return services.update_experiment(experiment, **validated_data)


class CreateExperimentSerializer(serializers.ModelSerializer):
    sessions = CreateSessionSerializer(many=True, required=False)
    title = serializers.CharField(required=False)

    class Meta:
        model = models.Experiment
        fields = (
            'description',
            'sessions',
            'title',
        )

    def create(self, validated_data):
        return services.create_experiment(**validated_data)

    def to_representation(self, experiment):
        return ExperimentSerializer(instance=experiment).data
