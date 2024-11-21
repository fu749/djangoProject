// 打开遮罩层
document.getElementById('resetPassword').addEventListener('click', function (event) {
event.preventDefault(); // 阻止链接的默认跳转行为
document.getElementById('passwordOverlay').classList.remove('hidden'); // 显示遮罩层
});


// 关闭遮罩层

document.getElementById('cancelPasswordChange').addEventListener('click', function () {
    document.getElementById('passwordOverlay').classList.add('hidden'); // 隐藏遮罩层
});

fetch('/change_password/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        user: user,
        current_password: '123',
        new_password: '123',
        confirm_password: '123'
    })
})
.then(response => response.json())
.then(data => {
    console.log(data);
})
.catch(error => {
    console.error('Error:', error);
});
