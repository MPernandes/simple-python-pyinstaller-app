pipeline {
    agent none

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.12-slim'
                    args '--user root'  // Jalankan sebagai root untuk izin penuh
                    reuseNode true      // Gunakan image lokal yang sudah ada
                }
            }
            steps {
                echo 'Memulai proses Build...'
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
                    args '--user root'
                    reuseNode true
                }
            }
            steps {
                echo 'Menjalankan pengujian (Test)...'
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

        stage('Deploy') {
            agent {
                docker {
                    image 'python:3.12-slim'
                    args '--user root'
                    reuseNode true
                }
            }
            steps {
                echo 'Menjalankan proses Deploy...'
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