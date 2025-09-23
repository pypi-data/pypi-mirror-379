from django.db.models import F

from huscy.project_design.models import (
    DataAcquisitionMethod,
    DataAcquisitionMethodType,
    Experiment,
    Session,
)


def create_experiment(project, description='', sessions=[], title=''):
    order = project.experiments.count()

    experiment = Experiment.objects.create(
        description=description,
        order=order,
        project=project,
        title=title or f'Experiment {order + 1}',
    )

    for session in sessions:
        create_session(experiment, **session)

    return experiment


def create_session(experiment, data_acquisition_methods=[], title='', contacts=[]):
    order = experiment.sessions.count()

    session = Session.objects.create(
        experiment=experiment,
        order=order,
        title=title or f'Session {order + 1}',
    )

    for data_acquisition_method in data_acquisition_methods:
        create_data_acquisition_method(session, **data_acquisition_method)

    session.contacts.set(contacts)

    return session


def create_data_acquisition_method(session, type, duration, location='', setup_time=None,
                                   teardown_time=None, stimulus=None):
    order = session.data_acquisition_methods.count()

    if isinstance(type, DataAcquisitionMethodType):
        pass
    elif isinstance(type, str):
        type = DataAcquisitionMethodType.objects.get(pk=type)
    else:
        raise ValueError('Unknown data type for `type` attribute')

    return DataAcquisitionMethod.objects.create(
        duration=duration,
        location=location,
        order=order,
        session=session,
        stimulus=stimulus,
        type=type,
    )


def delete_data_acquisition_method(data_acquisition_method):
    if data_acquisition_method.session.data_acquisition_methods.count() == 1:
        raise ValueError('The last remaining data acquisition method cannot be deleted.')
    (DataAcquisitionMethod.objects.filter(session=data_acquisition_method.session,
                                          order__gt=data_acquisition_method.order)
                                  .update(order=F('order') - 1))
    data_acquisition_method.delete()


def delete_experiment(experiment):
    (Experiment.objects.filter(project=experiment.project, order__gt=experiment.order)
                       .update(order=F('order') - 1))
    experiment.delete()


def delete_session(session):
    if session.experiment.sessions.count() == 1:
        raise ValueError('The last remaining session cannot be deleted.')
    (Session.objects.filter(experiment=session.experiment, order__gt=session.order)
                    .update(order=F('order') - 1))
    session.delete()


def get_experiments(project):
    return project.experiments.order_by('order')


def get_sessions(experiment):
    return experiment.sessions.order_by('order')


def get_data_acquisition_methods(session):
    return session.data_acquisition_methods.order_by('order')


def get_data_acquisition_method_type(short_name):
    return DataAcquisitionMethodType.objects.get(short_name=short_name)


def update_experiment(experiment, **kwargs):
    updatable_fields = (
        'description',
        'order',
        'title',
    )
    return update(experiment, updatable_fields, **kwargs)


def update_session(session, **kwargs):
    contacts = kwargs.pop('contacts', [])

    updatable_fields = (
        'title',
    )
    update(session, updatable_fields, **kwargs)

    session.contacts.set(contacts)

    return session


def update_data_acquisition_method(data_acquisition_method, **kwargs):
    updatable_fields = (
        'duration',
        'location',
        'setup_time',
        'stimulus',
        'teardown_time',
    )
    return update(data_acquisition_method, updatable_fields, **kwargs)


def update(instance, updatable_fields, **kwargs):
    update_fields = []

    for field_name, value in kwargs.items():
        if field_name not in updatable_fields:
            raise ValueError(f'Cannot update field "{field_name}".')
        setattr(instance, field_name, value)
        update_fields.append(field_name)

    if update_fields:
        instance.save(update_fields=update_fields)

    return instance
