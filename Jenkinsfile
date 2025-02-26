pipeline {
    agent none

    stages {
        stage('Checkout') {
            agent any
            steps {
                // Clone repository
                checkout scm
            }
        }

        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                    args '--user root'
                }
            }
            steps {
                sh 'ls -R' // Debug: cek struktur direktori
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.9'
                    args '--user root'
                }
            }
            steps {
                sh 'pip install pytest'
                sh 'pytest --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
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
                    image 'python:3.9'
                    args '--user root'
                }
            }
            steps {
                sh 'pip install pyinstaller'
                sh 'pyinstaller --onefile sources/add2vals.py'
            }
            post {
                success {
                    archiveArtifacts artifacts: 'dist/add2vals', fingerprint: true
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Membersihkan workspace setelah pipeline selesai
        }
    }
} 