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
    
    // real colours
    @State var realColours: [UIColor] = Array(repeating: .clear, count: 6)
    
    // estimated colours
    @State var estimatedColours: [UIColor] = Array(repeating: .clear, count: 6)
    
    var body: some View {
        VStack {
            VStack(spacing: 0) {
                Image(uiImage: UIImage(named: imgName)!)
                    .resizable()
                    .frame(width: 200, height: 200)
                    .padding()
                
                Text(infoString)
                    .padding()
                
                Divider()
                    .background(.white)
                    .frame(height: 2)
                
                // Real colours
                Text("Real Colours")
                HStack {
                    ForEach(0..<realColours.count, id: \.self) { index in
                        Rectangle()
                            .fill(Color(realColours[index]))
                            .frame(width: 20, height: 20)
                    }
                }
                .padding()
                
                // Estimated colours
                Divider()
                Text("Estimated Colours")
                VStack {
                    HStack {
                        ForEach(0..<estimatedColours.count, id: \.self) { index in
                            Rectangle()
                                .fill(Color(estimatedColours[index]))
                                .frame(width: 20, height: 20)
                        }
                    }
                    .padding()
                    Text(paletteString)
                }
                
                Divider()
                    .background(.white)
                    .frame(height: 2)
            }
            .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0, maxHeight: .infinity, alignment: .topLeading)
            .padding()
        }
        .padding()
        .onAppear {
            performColourAnalysis()
        }
    }
    
    func performColourAnalysis() {
        let image = UIImage(named: imgName)!
        let artwork = Artwork(image: image, title: imgTitle)
        
        viewModel.performAnalOnImage(artwork: artwork) { colourPairs in
            DispatchQueue.main.async {
                // Loop through the colourPairs and assign to real and estimated colours
                for i in 0..<min(colourPairs.count, realColours.count) {
                    realColours[i] = colourPairs[i].actualColourInfo.uiColour
                    estimatedColours[i] = colourPairs[i].estimatedColourInfo.uiColour
                    paletteString += "\(colourPairs[i].name), "
                }
            }
        }
    }
}
