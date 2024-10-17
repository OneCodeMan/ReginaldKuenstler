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
    
    // real
    @State var realColour1: UIColor = UIColor.red
    @State var realColour2: UIColor = UIColor.red
    @State var realColour3: UIColor = UIColor.red
    @State var realColour4: UIColor = UIColor.red
    @State var realColour5: UIColor = UIColor.red
    @State var realColour6: UIColor = UIColor.red
    
    // estimated
    @State var estimatedColour1: UIColor = UIColor.blue
    @State var estimatedColour2: UIColor = UIColor.blue
    @State var estimatedColour3: UIColor = UIColor.blue
    @State var estimatedColour4: UIColor = UIColor.blue
    @State var estimatedColour5: UIColor = UIColor.blue
    @State var estimatedColour6: UIColor = UIColor.blue

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
                    Rectangle()
                        .fill(Color(realColour1))
                        .frame(width: 20, height: 20)
                    Rectangle()
                        .fill(Color(realColour2))
                        .frame(width: 20, height: 20)
                    Rectangle()
                        .fill(Color(realColour3))
                        .frame(width: 20, height: 20)
                    Rectangle()
                        .fill(Color(realColour4))
                        .frame(width: 20, height: 20)
                    Rectangle()
                        .fill(Color(realColour5))
                        .frame(width: 20, height: 20)
                    Rectangle()
                        .fill(Color(realColour6))
                        .frame(width: 20, height: 20)
                }.padding()
                
                // Estimated colours
                Divider()
                Text("Estimated Colours")
                HStack {
                    Rectangle()
                        .fill(Color(estimatedColour1))
                        .frame(width: 20, height: 20)
                    Rectangle()
                        .fill(Color(estimatedColour2))
                        .frame(width: 20, height: 20)
                    Rectangle()
                        .fill(Color(estimatedColour3))
                        .frame(width: 20, height: 20)
                    Rectangle()
                        .fill(Color(estimatedColour4))
                        .frame(width: 20, height: 20)
                    Rectangle()
                        .fill(Color(estimatedColour5))
                        .frame(width: 20, height: 20)
                    Rectangle()
                        .fill(Color(estimatedColour6))
                        .frame(width: 20, height: 20)
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
            vm.performAnalOnImage(artwork: artwork) { colourPair in
                DispatchQueue.main.async {
                    print("colourPair is:\n\(colourPair)")
                    // display real colours
                    self.realColour1 = colourPair[0].actualColourInfo.uiColour
                    self.realColour2 = colourPair[1].actualColourInfo.uiColour
                    self.realColour3 = colourPair[2].actualColourInfo.uiColour
                    self.realColour4 = colourPair[3].actualColourInfo.uiColour
                    self.realColour5 = colourPair[4].actualColourInfo.uiColour
                    self.realColour6 = colourPair[5].actualColourInfo.uiColour
                    
                    // display estimated colours
                    self.estimatedColour1 = colourPair[0].estimatedColourInfo.uiColour
                    self.estimatedColour2 = colourPair[1].estimatedColourInfo.uiColour
                    self.estimatedColour3 = colourPair[2].estimatedColourInfo.uiColour
                    self.estimatedColour4 = colourPair[3].estimatedColourInfo.uiColour
                    self.estimatedColour5 = colourPair[4].estimatedColourInfo.uiColour
                    self.estimatedColour6 = colourPair[5].estimatedColourInfo.uiColour
                }
            }
        }
    }
}

#Preview {
    ContentView()
}
