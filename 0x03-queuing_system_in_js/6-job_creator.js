import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    'phoneNumber': 'string',
    'message': 'string'
};

const pushNotificationJob = queue.create('push_notification_job', jobData)
    .save(err => {
        if (!err) {
            console.log(`Notification job created: ${pushNotificationJob.id}`);
        } else {
            console.log('Notification job failed');
    }
    });
