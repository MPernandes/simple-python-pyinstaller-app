node {
    stage('Prepare Environment') {
        sh 'docker pull python:3.9-slim'
    }

    stage('Build') {
        docker.image('python:3.9-slim').inside('--user root -p 5000:5000') {
            sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                python -m py_compile sources/add2vals.py sources/calc.py
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            '''
        }
    }

    stage('Test') {
        docker.image('python:3.9-slim').inside('-p 5000:5000') {
            sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
        }
    }
}