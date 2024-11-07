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
    @ObservedObject var viewModel = AveragePaletteViewModel()
    @State var masterPalette: MasterPalette = MasterPaletteConstants.masterPalettes[0]
    let rows = [GridItem(.flexible(minimum: UIScreen.main.bounds.width))]
    
    // MARK: Dismiss state
    @Environment(\.dismiss) var dismiss
    
    // MARK: States for auto-scrolling
    @State var enableAutoscrollShenanigans: Bool = true
    @State var isPaletteInformationFullScreen: Bool = false
    
    @State var currentIndexCarousel: Int = 0
    
    var body: some View {
        NavigationStack {
            ZStack {
                ScrollViewReader { proxy in
                    ScrollView(.horizontal) {
                        LazyHGrid(rows: rows, spacing: 0) {
                            ForEach(masterPalette.imageStrings.indices, id: \.self) { index in
                                
                                ZStack {
//                                    if index == 0 {
//                                        Text(masterPalette.lifespan)
//                                            .font(.system(size: 50.0))
//                                    }
                                    Image(masterPalette.imageStrings[index])
                                        .resizable()
                                        .scaledToFill()
                                        .frame(minWidth: UIScreen.main.bounds.width, maxWidth: .infinity, minHeight: UIScreen.main.bounds.height)
                                        .clipped()
                                        .id(index)
                                }
                                
                            }
                        }
                    }
                    .onTapGesture {
                        self.enableAutoscrollShenanigans = false
                    }
                    .onAppear {
                        
                        // NOTE: this is for debugging when u wanna fill the hardcodedgreatspalettedata
//                        Task {
//                            var imagesToAnalyze: [UIImage] = []
//                            for imageString in masterPalette.imageStrings {
//                                if let generatedImage = UIImage(named: imageString) {
//                                    imagesToAnalyze.append(generatedImage)
//                                } else {
//                                    print("could not generate image")
//                                }
//                            }
//                            
//                            await viewModel.analyzeImages(images: imagesToAnalyze)
//                        }
                        
                        
                        // MARK: Scrolling onAppear stuff
                        // TODO: lmfao
                        // Scroll a bit to the next image
                        if enableAutoscrollShenanigans {
                            
                            
                            DispatchQueue.main.asyncAfter(deadline: .now() + 1.0) {
                                withAnimation(.smooth(duration: 4.0)) {
                                    proxy.scrollTo(0, anchor: .center)
                                }
                                
                                DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
                                    withAnimation(.smooth(duration: 4.0)) {
                                        proxy.scrollTo(0, anchor: .trailing)
                                    }
                                    
                                    DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
                                        withAnimation(.easeOut(duration: 4.0)) {
                                            proxy.scrollTo(1, anchor: .leading)
                                            
                                            // self.startautomaticscrolling = true
                                        }
                                    }
                                    
                                }
                            }
                            
                        }
                        
                    }
                }
                .edgesIgnoringSafeArea(.all)
                .navigationBarBackButtonHidden(true)
                .toolbar(.hidden, for: .tabBar)
                .toolbar {
                    if !isPaletteInformationFullScreen {
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
                    
                }
                
            } // ZStack
            // TODO: minimum palette...
            .overlay(PaletteOfGreatView(minimumPalette: $masterPalette.minimumPalette, artistName: $masterPalette.artistName, isFullScreen: $isPaletteInformationFullScreen, currentIndexScrollView: $currentIndexCarousel), alignment: .bottom)
        }
        .statusBar(hidden: true)
    }
}


struct PaletteOfGreatView: View {
    @Binding var minimumPalette: Palette
    @Binding var artistName: String
    @Binding var isFullScreen: Bool
    @Binding var currentIndexScrollView: Int
    
    var shouldOmitTitle: Bool = false
    @Environment(\.colorScheme) var colorScheme
    
    // MARK: Fullscreen states for view
    private let columns = Array(repeating: GridItem(.flexible()), count: 3)

    var body: some View {
        VStack(alignment: .center) {
            if self.isFullScreen {
                ScrollView {
                    VStack {
                        Spacer()
                        if !shouldOmitTitle {
                            Text("The \(artistName) Palette")
                                .font(.defaultFontLargeTitle)
                                .padding(.bottom, 8)
                                .foregroundStyle(colorScheme == .light ? Color.black : Color.white)
                            
                        }
                        
                        LazyVGrid(columns: self.columns) {
                            ForEach(minimumPalette.colours, id: \.self) { pc in
                                SingularPaletteItemView(paletteColour: pc)
                            }
                        }
                        
                    }// .frame(minWidth: UIScreen.main.bounds.width)
                    .padding()
                    
                }.frame(minWidth: UIScreen.main.bounds.width)
               
            } else {
                // NOT fullscreen
                
                // Bottom HStack
                HStack(alignment: .bottom) {
                    if minimumPalette.colours.count >= 5 {
                        ForEach(Array(minimumPalette.colours.prefix(upTo: 6)), id: \.self) { pc in
                            SingularPaletteItemView(paletteColour: pc, circleOpacity: 0.2, omitColourName: true)
                        }
                    }
                    
                } // HStack
                .frame(maxWidth: .infinity)
                .frame(height: 50)
                .padding()
                
            }
             // end of else
            
        }
        .background(colorScheme == .light ? (isFullScreen ? Color.white.opacity(0.9) : Color.white.opacity(0.15)) : (isFullScreen ? Color.black.opacity(0.9) : Color.black.opacity(0.15)))
        .onTapGesture {
            withAnimation(.easeOut(duration: 1.0)) {
                self.isFullScreen.toggle()
            }
        }
        // VSTACK
    }
}
