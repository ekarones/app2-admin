const modalImage = document.getElementById("modal-image");
const modalImageButtons = document.getElementsByClassName("show-image-btn");
const openModalImage = document.getElementById("open-modal-image");
const closeModalImage = document.getElementById("close-modal-image");
const RefImage = document.getElementById("ref-image");

Array.from(modalImageButtons).forEach((button) => {
  button.addEventListener("click", function (event) {
    const api_url = this.getAttribute("data-api-url");
    const img_name = this.getAttribute("data-image-name");
    const image_url = `${api_url}?filename=${img_name}`;

    RefImage.src = image_url;
    modalImage.style.display = "flex";
  });
});
closeModalImage.addEventListener("click", () => {
  modalImage.style.display = "none";
});
