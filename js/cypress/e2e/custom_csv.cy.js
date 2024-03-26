
const urls = [
    "https://gettyimages.in/detail/video/crowds-flee-from-police-tear-gas-grenades-a-general-strike-in-to-video/677557362____677557362.mp4"
  ];
  
  describe('Download Functionality Test for Multiple URLs', () => {
    urls.forEach((url) => {
      it(`should download a video from ${url}`, () => {
        const parts = url.split('____');
        const videoId = parts[1].split('.')[0]; 
        cy.visit(url);
        cy.get('.f05EVVQW8iYfSZTUwEJ_').click();
        cy.get('#hide-comp-license').click();
        cy.get('.OfSHWBOuuOsBlJjyVeCc').click();
        cy.wait(5000);

        cy.exec(`mv downloads/*.mp4 ~/Downloads/${videoId}.mp4`);
      });
    });
  });