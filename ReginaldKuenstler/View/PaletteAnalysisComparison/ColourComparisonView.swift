//
//  ColourComparisonView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import SwiftUI
import SwiftVibrantium

struct ColourComparisonView: View {
    @ObservedObject var viewModel = KuenstlerViewModel()
    @State var imgTitle = "Calum from Aftersun"
    @State var imgName = "starz"
    @State var infoString = "Title of Image"
    @State var paletteString = ""
    @State var personalPaletteString = ""
    
    // Put this data in viewmodel.
    // real colours
    @State var realColours: [UIColor] = Array(repeating: .clear, count: 6)
    
    // estimated colours
    @State var estimatedColours: [UIColor] = Array(repeating: .clear, count: 6)
    
    // from user palette
    @State var coloursFromUserPalette: [UIColor] = Array(repeating: .clear, count: 6)
    
    
    // image picker related
    @State private var image = UIImage(named: "beauty") ?? UIImage()
    @State private var showSheet = false
    @State private var showImagePicker = false
    @State private var sourceType: UIImagePickerController.SourceType = .photoLibrary
    // end of img picker related
    
    var body: some View {
        CarouselView(views:
                        [CarouselPage(id: 1,
                                      content:
                                        {
            ImageAnalysisInputView(image: $image, showSheet: $showSheet, handdleAnalyzePhoto: { self.performColourAnalysis(onImage: self.image) })
                .actionSheet(isPresented: $showSheet) {
                    ActionSheet(title: Text("Select Photo"), message: Text("Choose an option"), buttons: [
                        .default(Text("Take Photo")) {
                            self.sourceType = .camera
                            self.showImagePicker = true
                        },
                        .default(Text("Select from Library")) {
                            self.sourceType = .photoLibrary
                            self.showImagePicker = true
                        },
                        .cancel()
                    ])
                }
                .sheet(isPresented: $showImagePicker) {
                    ImagePicker(sourceType: self.sourceType, selectedImage: self.$image)
                }
                .onAppear {
                    self.performColourAnalysis(onImage: self.image)
                }
        }
                                     ),
                         CarouselPage(id: 2,
                                      content: {
            PaletteResults(realColours: $realColours, paletteString: $paletteString, coloursFromUserPalette: $coloursFromUserPalette, personalPaletteString: $personalPaletteString)
        }
                                     ),
                         CarouselPage(id: 3, content: { EmptyView() })]
        )
    }
    
    func performColourAnalysis(onImage img: UIImage) {
        // let image = UIImage(named: imgName)!
        
        // reset palette strings
        paletteString = ""
        personalPaletteString = ""
        let artwork = Artwork(image: img, title: imgTitle)
        
        viewModel.performAnalOnImage(artwork: artwork) { colourPairs, relevantColoursFromUserPalette in
            DispatchQueue.main.async {
                // Loop through the colourPairs and assign to real and estimated colours
                for i in 0..<min(colourPairs.count, realColours.count) {
                    realColours[i] = colourPairs[i].actualColourInfo.uiColour
                    estimatedColours[i] = colourPairs[i].estimatedColourInfo.uiColour
                    paletteString += "\(colourPairs[i].name), "
                }
                
                if !relevantColoursFromUserPalette.isEmpty {
                    for (j, relevantColour) in relevantColoursFromUserPalette.enumerated() {
                        coloursFromUserPalette[j] = relevantColour.uiColour
                        personalPaletteString += "\(relevantColoursFromUserPalette[j].name), "
                    }
                } else {
                    coloursFromUserPalette = []
                    personalPaletteString = "No relevant colours found."
                }
                
            }
        }
    }
}

// first page in carousel
struct ImageAnalysisInputView: View {
    @Binding var image: UIImage
    @Binding var showSheet: Bool
    var handdleAnalyzePhoto: () -> ()
    
    var body: some View {
        ZStack {
            Image(uiImage: self.image)
                .resizable()
                .aspectRatio(image.size, contentMode: .fill)
                .edgesIgnoringSafeArea(.all)
                .statusBar(hidden: true)
                .clipShape(Rectangle())
                .padding()
            
            VStack {
                Text("Change photo")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .frame(height: 50)
                    .background(LinearGradient(gradient: Gradient(colors: [Color(#colorLiteral(red: 0.262745098, green: 0.0862745098, blue: 0.8588235294, alpha: 1)), Color(#colorLiteral(red: 0.5647058824, green: 0.462745098, blue: 0.9058823529, alpha: 1))]), startPoint: .top, endPoint: .bottom))
                    .cornerRadius(16)
                    .foregroundColor(.white)
                    .padding(.horizontal, 20)
                    .onTapGesture {
                        showSheet = true
                    }
                
                Text("Analyze")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .frame(height: 50)
                    .background(LinearGradient(gradient: Gradient(colors: [Color(#colorLiteral(red: 0.262745098, green: 0.0862745098, blue: 0.8588235294, alpha: 1)), Color(#colorLiteral(red: 0.5647058824, green: 0.462745098, blue: 0.9058823529, alpha: 1))]), startPoint: .top, endPoint: .bottom))
                    .cornerRadius(16)
                    .foregroundColor(.white)
                    .padding(.horizontal, 20)
                    .onTapGesture {
                        print("Analyze button tapped, performing analysis on \(self.image)")
                        handdleAnalyzePhoto()
                    }
            }
            .padding()
            .frame(maxHeight: .infinity, alignment: .bottom)
            
        }
    }
}

// second page in carousel
struct PaletteResults: View {
    @Binding var realColours: [UIColor]
    @Binding var paletteString: String
    @Binding var coloursFromUserPalette: [UIColor]
    @Binding var personalPaletteString: String
    var body: some View {
        ScrollView {
            VStack(alignment: .center) {
                Text("Detected Colours")
                    .font(.title2)
                
                HStack(spacing: 0) {
                    ForEach(0..<realColours.count, id: \.self) { index in
                        Rectangle()
                            .fill(Color(realColours[index]))
                            .frame(minWidth: 50, minHeight: 300)
                    }
                }
                .padding()
                .frame(maxWidth: .infinity)
                
                
                Text(paletteString)
                    .padding()
                
                Text("From Your Palette")
                VStack {
                    HStack(alignment: .center) {
                        ForEach(0..<coloursFromUserPalette.count, id: \.self) { index in
                            Rectangle()
                                .fill(Color(coloursFromUserPalette[index]))
                                .frame(width: 20, height: 20)
                        }
                    }
                    .padding()
                    Text(personalPaletteString)
                }
            }
        }
    }
}
