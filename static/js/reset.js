document.addEventListener('DOMContentLoaded', () => {
  const overlay = document.getElementById('overlay');
  const changePasswordButton = document.getElementById('changePasswordButton');
  const cancelButton = document.getElementById('cancelButton');
  const passwordForm = document.getElementById('passwordForm');

  // 显示遮罩和表单
  changePasswordButton.addEventListener('click', () => {
    overlay.classList.remove('hidden');
  });

  // 取消按钮关闭遮罩
  cancelButton.addEventListener('click', () => {
    overlay.classList.add('hidden');
  });

  // 提交表单
  passwordForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // 简单校验
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (newPassword !== confirmPassword) {
      alert('两次密码输入不一致！');
      return;
    }

    alert('密码修改成功！');
    overlay.classList.add('hidden');
    passwordForm.reset();
  });
});
