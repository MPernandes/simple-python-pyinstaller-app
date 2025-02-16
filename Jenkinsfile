node {
    stage('Build') {
        docker.image('python:2-alpine').inside {
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }

    stage('Test') {
        docker.image('qnib/pytest').inside {
            sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
        }
    }

    stage('Publish Results') {
        junit 'test-reports/results.xml'
    }

    stage('Deploy') {
        try {
            docker.image('cdrx/pyinstaller-linux:python2').inside {
                sh 'pyinstaller --onefile sources/add2vals.py'
            }

            // Mengarsipkan hasil build jika sukses
            archiveArtifacts 'dist/add2vals'
        } catch (err) {
            echo "Pipeline gagal: ${err}"
            currentBuild.result = 'FAILURE'
        }
    }
}
