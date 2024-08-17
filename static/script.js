document.getElementById('file-upload').addEventListener('change', function() {
    const fileName = this.files[0] ? this.files[0].name : 'No file chosen';
    document.getElementById('file-name').textContent = fileName;
});

document.getElementById('upload-form').addEventListener('submit', function(event) {
    const fileInput = document.getElementById('file-upload');
    const errorMessage = document.getElementById('error-message');
    if (!fileInput.files.length) {
        event.preventDefault();
        errorMessage.textContent = 'Please choose an image file';
    } else {
        errorMessage.textContent = ''; 
    }
});

document.getElementById('detail-button')?.addEventListener('click', function() {
    const details = document.getElementById('disease-details');
    details.classList.toggle('show');
    this.textContent = details.classList.contains('show') ? 'Hide Details' : 'Show Details';
});

// Hiển thị kết quả mượt mà và cuộn đến kết quả
const resultContainer = document.getElementById('result-container');
if (resultContainer) {
    resultContainer.classList.add('show');

    resultContainer.scrollIntoView({
        behavior: 'smooth',
        block: 'start' 
    });
}

document.getElementById('report-button').addEventListener('click', function() {
    document.getElementById('report-form').style.display = 'block';
});

function submitReport() {
    // Lấy thông tin từ biểu mẫu báo cáo
    var reportText = document.getElementById('report-text').value;

    if (reportText.trim() === "") { 
        alert("Please enter information to report");
        return; // Không gửi báo cáo nếu chưa có thông tin
    }
    // Gửi thông tin báo cáo đến máy chủ (bạn cần triển khai phần xử lý phía máy chủ)
    // Sử dụng fetch API:
    fetch('/report', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ report: reportText })
    })
    .then(response => {
        // Xử lý phản hồi từ máy chủ
    })
    .catch(error => {
        // Xử lý lỗi
    });
    document.getElementById('report-form').style.display = 'none';
            alert('Thank you for your report!');
        }