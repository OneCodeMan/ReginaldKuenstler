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
    @State var images: [String] = MasterPaletteConstants.hopperImageStrings
    let rows = [GridItem(.flexible(minimum: UIScreen.main.bounds.width))]
    
    // MARK: Dismiss state
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        NavigationStack {
            ZStack {
                ScrollView(.horizontal) {
                    LazyHGrid(rows: rows, spacing: 0) {
                        ForEach(images, id: \.self) { image in
                            Image(image)
                                .resizable()
                                .scaledToFill()
                                .frame(minWidth: UIScreen.main.bounds.width, maxWidth: .infinity, minHeight: UIScreen.main.bounds.height) // Fill most of the screen
                                .clipped()
                        }
                    }
                }
                .edgesIgnoringSafeArea(.all) // Makes images fill edge to edge
                .navigationBarBackButtonHidden(true) // hide the back button
                .toolbar(.hidden, for: .tabBar)
                .toolbar {
                    // Add a toolbar item for the cancel button
                    ToolbarItem(placement: .navigationBarLeading) {
                        Button {
                            self.dismiss()
                        } label: {
                            HStack {
                                Image(systemName: "chevron.backward")
                                    .aspectRatio(contentMode: .fit)
                                    .foregroundColor(.white)
                            }
                        }
                    }
                }
                
                
            } // ZStack
            .overlay(PaletteOfGreatView(minimumPalette: Palette.mockPalette), alignment: .bottom)
        }
        .statusBar(hidden: true)
    }
}


struct PaletteOfGreatView: View {
    var minimumPalette: Palette
    var body: some View {
        VStack {
            // Bottom HStack
            HStack(alignment: .bottom) {
                ForEach(minimumPalette.colours, id: \.self) { pc in 
                    SingularPaletteItemView(paletteColour: pc)
                }
                
            } // HStack
            .frame(height: 50)
            .frame(maxWidth: .infinity)
            .padding()
            .background(Color.white.opacity(0.4))
        }
        // VSTACK
    }
}
