function openEbook(pdfUrl) {
    var modal = document.getElementById("ebookModal");
    var pdfViewer = document.getElementById("pdfViewer");
    pdfViewer.setAttribute("src", pdfUrl);
    modal.style.display = "block";
}

function closeEbook() {
    var modal = document.getElementById("ebookModal");
    modal.style.display = "none";
}

function confirmDelete(bookId) {
    var modal = document.getElementById("deleteModal");
    modal.style.display = "block";

    var confirmButton = document.getElementById("confirmDeleteButton");
    confirmButton.onclick = function() {
        modal.style.display = "none"; // 确认删除后先关闭模态框
        deleteBook(bookId); // 然后再执行删除操作
    };
}

function closeDelete() {
    var modal = document.getElementById("deleteModal");
    modal.style.display = "none";
}

function deleteBook(bookId) {
    fetch(`/delete_book/${bookId}/`, {
        method: 'DELETE', // 使用 DELETE 方法删除资源
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    }).then(response => {
        if (response.ok) {
            window.location.reload(); // 删除成功后刷新页面
        } else {
            alert("刪除失敗");
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
