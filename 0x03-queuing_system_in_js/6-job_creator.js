import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    'phoneNumber': '+1234567890',
    'message': 'This is the code to verify your account'
};

const pushNotificationJob = queue.create('push_notification_job', jobData)
    .save(err => {
        if (!err) {
            console.log(`Notification job created: ${pushNotificationJob.id}`);
        } else {
            console.log('Notification job failed');
    }
    });
