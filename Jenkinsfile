pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.12-slim'
                }
            }
            steps {
                echo '🚀 Memulai proses Build...'
                sh '''
                   python -m pip install --upgrade pip
                   python -m py_compile sources/add2vals.py sources/calc.py
                '''
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:3.12-slim'
                }
            }
            steps {
                echo '✅ Menjalankan Pengujian...'
                sh '''
                   python -m pip install pytest
                   mkdir -p test-reports
                   pytest --verbose --junit-xml test-reports/results.xml sources/test_calc.py || exit 1
                '''
            }
            post {
                always {
                    echo '📊 Mengarsipkan hasil pengujian...'
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            agent {
                docker {
                    image 'python:3.12-slim'
                }
            }
            steps {
                echo '📦 Membuat binary dengan PyInstaller...'
                sh '''
                    python -m pip install pyinstaller
                    pyinstaller --onefile sources/add2vals.py
                    ls -lh dist/
                '''
            }
            post {
                success {
                    echo '📂 Mengarsipkan binary...'
                    archiveArtifacts artifacts: 'dist/add2vals', fingerprint: true
                }
                failure {
                    echo '❌ Gagal membuat binary. Periksa log.'
                }
            }
        }
    }
}