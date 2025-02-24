pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.12-slim'
                    args '--dns 8.8.8.8 --dns 8.8.4.4'
                }
            }
            steps {
                sh '''
                   mkdir -p sources/__pycache__
                   python -m py_compile sources/add2vals.py sources/calc.py
                '''
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                    args '--dns 8.8.8.8 --dns 8.8.4.4'
                }
            }
            steps {
                sh '''
                   mkdir -p test-reports
                   py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py
                '''
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage('Deliver') {
            agent {
                docker {
                    image 'python:3.12-slim'
                    args '--dns 8.8.8.8 --dns 8.8.4.4'
                }
            }
            steps {
                sh '''
                   python -m pip install pyinstaller
                   pyinstaller --onefile sources/add2vals.py
                '''
            }
            post {
                success {
                    archiveArtifacts 'dist/add2vals'
                }
            }
        }
    }
}