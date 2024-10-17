//
//  ContentView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-15.
//

import SwiftUI
import SwiftVibrantium

struct ContentView: View {
    @State var imgTitle = ""
    @State var imgName = ""
    @State var infoString = "Title of Image"
    
    // real colours
    @State var realColours: [UIColor] = Array(repeating: .clear, count: 6)
    
    // estimated colours
    @State var estimatedColours: [UIColor] = Array(repeating: .clear, count: 6)
    
    // titles
    
    var body: some View {
        VStack {
            VStack(spacing: 0) {
                Image(uiImage: UIImage(named: "starz")!)
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
                }.padding()
                
                // Estimated colours
                Divider()
                Text("Estimated Colours")
                HStack {
                    ForEach(0..<realColours.count, id: \.self) { index in
                        Rectangle()
                            .fill(Color(estimatedColours[index]))
                            .frame(width: 20, height: 20)
                    }
                }.padding()
                Divider()
                    .background(.white)
                    .frame(height: 2)
            }
            .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0, maxHeight: .infinity, alignment: .topLeading)
            .padding()
        }
        .padding()
        .onAppear {
            let vm = KuenstlerViewModel()
            self.imgTitle = "Calum from Aftersun"
            self.imgName = "starz"
            let image = UIImage(named: imgName)!
            let artwork = Artwork(image: image, title: imgTitle)
            
            // colourPairs is an aray
            vm.performAnalOnImage(artwork: artwork) { colourPairs in
                DispatchQueue.main.async {
                    print("colourPairs are :\n\(colourPairs)\n\n\n")
                    // display real colours
                    // Loop through the colourPairs and assign to real and estimated colours
                    for i in 0..<min(colourPairs.count, realColours.count) {
                        realColours[i] = colourPairs[i].actualColourInfo.uiColour
                        estimatedColours[i] = colourPairs[i].estimatedColourInfo.uiColour
                    }
                }
            }
        }
    }
}

#Preview {
    ContentView()
}
