node {
    stage('Prepare Environment') {
        sh 'docker pull python:3.9-slim'
    }

    stage('Build') {
        docker.image('python:3.9-slim').inside('-p 5000:5000') {
            try {
                sh 'pip install -r requirements.txt'
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
                stash name: 'compiled-results', includes: 'sources/*.py*'
            } catch (Exception e) {
                error "Build failed: ${e}"
            }
        }
    }

    stage('Test') {
        docker.image('python:3.9-slim').inside('-p 5000:5000') {
            try {
                sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
            } catch (Exception e) {
                error "Test failed: ${e}"
            } finally {
                junit 'test-reports/results.xml'
            }
        }
    }
}