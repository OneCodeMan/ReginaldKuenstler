//
//  ReginaldKuenstlerTabView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

/**
 Two tabs:
 - your palette
 - image generator.
 */

import SwiftUI

struct ReginaldKuenstlerTabView: View {
    @EnvironmentObject var userPaletteViewModel: UserPaletteViewModel // Access the ViewModel

    @State var selectedTab: Int = 0
    var body: some View {
        TabView(selection:  $selectedTab) {
            UserPaletteView()
                .environmentObject(userPaletteViewModel)
                .tag(0)
                .tabItem {
                    Image(systemName: "paintpalette.fill")
                        .renderingMode(.template)
                        .foregroundColor(.red) // <2>
                    // TODO: Localize me
                    Text("Your Palette")
                }
                .font(.defaultFontCaption)
            
            ColourComparisonView()
                .environmentObject(userPaletteViewModel)
                .tag(1)
                .tabItem {
                    Image(systemName: "chart.bar.fill")
                        .renderingMode(.template)
                    // TODO: Localize me
                    Text("Analyzer")
                }
                .font(.defaultFontCaption)
            
//            MessageView()
//                .tag(2)
//                .tabItem {
//                    Image(systemName: "person.fill.questionmark")
//                    Text("TO YOU")
//                }
        }
        .tint(.indigo)
    }
}

#Preview {
    ReginaldKuenstlerTabView()
}
