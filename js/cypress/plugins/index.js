const fileUpload = require('cypress-file-upload');

module.exports = (on, config) => {
  on('file:preprocessor', fileUpload());
};