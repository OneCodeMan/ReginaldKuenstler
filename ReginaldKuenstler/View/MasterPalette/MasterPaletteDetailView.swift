//
//  MasterPaletteDetailView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-11-02.
//


/*
 LOL
 https://gist.github.com/cjnevin/fc416e31cfcfb7f5f60a1fb401926f79
 https://stackoverflow.com/questions/68409874/can-i-create-a-scrollview-that-is-infinite-scrolling-but-has-fixed-values
 */

import SwiftUI

/*
 Horizontal Images carousel
 */
struct MasterPaletteDetailView: View {
    // let images = ["caravaggio0", "caravaggio1", "caravaggio2", "caravaggio3", "caravaggio4", "caravaggio5"]
    
    @State var images: [String] = MasterPaletteConstants.hopperImageStrings
    
    let rows = [GridItem(.flexible(minimum: UIScreen.main.bounds.width))]
    
    var body: some View {
        ScrollView(.horizontal) {
            LazyHGrid(rows: rows, spacing: 0) {
                ForEach(images, id: \.self) { image in
                    Image(image)
                        .resizable()
                        .scaledToFill()
                        .frame(minWidth: UIScreen.main.bounds.width ,maxWidth: .infinity, minHeight: UIScreen.main.bounds.height) // Fill most of the screen
                        .clipped()
                }
            }
        }
        .edgesIgnoringSafeArea(.all) // Makes images fill edge to edge
        .toolbar(.hidden, for: .tabBar)
        .statusBarHidden()
        .onAppear {
            
        }
    }
    
}
