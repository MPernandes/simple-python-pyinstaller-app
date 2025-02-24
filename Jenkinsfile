pipeline {
    agent none

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2.7'
                    args '--user root' // Akses root di dalam container
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
                    image 'cdrx/pyinstaller-linux:python2'
                    args '--user root'
                }
            }
            steps {
                echo 'Menjalankan proses Deploy...'
                sh '''
                   mkdir -p dist
                   pyinstaller --onefile sources/add2vals.py
                '''
            }
            post {
                success {
                    echo 'Mengarsipkan hasil build...'
                    archiveArtifacts 'dist/add2vals'
                }
                failure {
                    echo 'Deploy gagal!'
                }
            }
        }
    }
}