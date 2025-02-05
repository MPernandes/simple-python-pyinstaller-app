node {
    try {
        stage('Checkout') {
            git 'https://github.com/MPernandes/simple-python-pyinstaller-app.git'
        }

        stage('Install Python3 and Pip3') {
            sh '''
                sudo apt update
                sudo apt install -y python3 python3-pip
            '''
        }

        stage('Install Dependencies') {
            sh 'pip3 install -r requirements.txt'
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