node {
    stage('Prepare Environment') {
        sh 'docker pull python:3.9-slim'
    }

    stage('Build') {
        docker.image('python:3.9-slim').inside('-p 5000:5000') {
            sh 'pip install -r requirements.txt'
        }
    }

    stage('Test') {
        docker.image('python:3.9-slim').inside('-p 5000:5000') {
            sh './jenkins/scripts/test.sh'
        }
    }
}