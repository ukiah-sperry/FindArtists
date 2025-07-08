const fileInput = document.getElementById("file-input");
const uploadBtn = document.getElementById("upload-btn");

fileInput.addEventListener("change", () => {
if (fileInput.files.length) {
    uploadBtn.disabled = false;
}
});
