node {
    try {
        stage('Build Docker Image') {
            // Bangun Docker image
            sh 'docker build -t python-app .'
        }

        stage('Run Unit Tests') {
            // Jalankan container untuk testing
            sh 'docker run --rm python-app python -m unittest discover -s .'
        }

        stage('Push to Docker Hub') {
            withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                sh 'docker tag python-app user/python-app:latest'  // Ganti 'user' dengan Docker Hub username
                sh 'docker push user/python-app:latest'
            }
        }

        stage('Deploy') {
            // Jalankan container di server
            sshagent(['server-ssh-key']) {
                sh '''
                ssh user@server << EOF
                docker pull user/python-app:latest
                docker stop python-app || true
                docker rm python-app || true
                docker run -d -p 5100:5000 --name python-app user/python-app:latest
                EOF
                '''
            }
        }

        stage('Clean Up') {
            // Hapus image lokal yang tidak diperlukan
            sh 'docker rmi python-app'
        }
        
        echo "✅ Deployment sukses!"
        
    } catch (err) {
        echo "❌ Pipeline gagal: ${err}"
        currentBuild.result = 'FAILURE'
    }
}