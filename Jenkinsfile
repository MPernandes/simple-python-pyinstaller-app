node {
    stage('Build') {
        try {
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            stash name: 'compiled-results', includes: 'sources/*.py*'
        } catch (Exception e) {
            error "Build failed: ${e}"
        }
    }

    stage('Test') {
        try {
            sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
        } catch (Exception e) {
            error "Test failed: ${e}"
        } finally {
            junit 'test-reports/results.xml'
        }
    }
}