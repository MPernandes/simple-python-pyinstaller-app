node {
    try {
        stage('Checkout') {
            git 'https://github.com/MPernandes/simple-python-pyinstaller-app.git'
        }

        stage('Install Dependencies') {
            sh 'pip install -r requirements.txt'
        }

        stage('Build Executable') {
            sh 'pyinstaller --onefile your_script.py'
        }

        stage('Test') {
            // Example test command, replace with actual tests
            sh 'pytest tests/'
        }

        stage('Archive Artifacts') {
            archiveArtifacts allowEmptyArchive: true, artifacts: 'dist/*'
        }
    } catch (Exception e) {
        currentBuild.result = 'FAILURE'
        throw e
    } finally {
        cleanWs()
    }
}