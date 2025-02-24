pipeline {
    agent none

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2.7'
                }
            }
            steps {
                echo 'Memulai proses Build...'
                sh '''
                   mkdir -p sources/__pycache__
                   python -m py_compile sources/add2vals.py sources/calc.py
                   ls -lh sources/__pycache__
                '''
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                echo 'Menjalankan pengujian (Test)...'
                sh '''
                   mkdir -p test-reports
                   py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py || exit 1
                '''
            }
            post {
                always {
                    echo 'Mengarsipkan hasil pengujian...'
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage('Deploy') {
            agent {
                docker {
                    image 'python:2.7'
                }
            }
            steps {
                echo 'Memulai proses Deploy...'
                sh '''
                    python -m pip install --upgrade pip
                    python -m pip install pyinstaller
                    pyinstaller --onefile sources/add2vals.py
                    ls -lh dist/
                '''
            }
            post {
                success {
                    echo 'Mengarsipkan hasil deploy...'
                    archiveArtifacts artifacts: 'dist/add2vals', fingerprint: true
                }
                failure {
                    echo 'Gagal deploy! Periksa log untuk detailnya.'
                }
            }
        }
    }
}