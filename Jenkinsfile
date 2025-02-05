node {
    stage('Prepare Environment') {
        sh 'docker pull python:3.9-slim'
    }

    stage('Build') {
        docker.image('python:3.9-slim').inside('--user root -p 5000:5000') {
            sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                pip3 install -r requirements.txt
            '''
        }
    }

    stage('Test') {
        docker.image('python:3.9-slim').inside('-p 5000:5000') {
            sh './jenkins/scripts/test.sh'
        }
    }
}