node {
    stage('Build') {
        docker.image('python:2-alpine').inside('--user root') {
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }

    stage('Test') {
        docker.image('qnib/pytest').inside('--user root') {
            try {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            } finally {
                junit 'test-reports/results.xml'
            }
        }
    }

    stage('Manual Approval') {
        input message: 'Lanjutkan ke tahap Deploy? (Klik "Proceed" untuk lanjut)'
    }

    stage('Deploy') {
        docker.image('python:3.9').inside('--user root') {
            sh 'pip install pyinstaller'
            sh 'pyinstaller --onefile sources/add2vals.py'
            archiveArtifacts 'dist/add2vals'

            // Menjeda eksekusi selama 1 menit setelah deploy
            echo 'Menunggu 1 menit agar aplikasi berjalan...'
            sleep(time: 1, unit: 'MINUTES')
            echo 'Proses deploy selesai, pipeline berhasil!'
        }
    }
}
