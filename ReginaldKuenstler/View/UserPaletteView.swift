//
//  UserPalette.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

/**
 Either a list of palettes or an empty view.
 The list of palettes comes from UserDefaults.
 */

import SwiftUI

struct UserPaletteView: View {
    @ObservedObject var userPaletteViewModel = UserPaletteViewModel()
    
    // MARK: search logic
    @State var searchText: String = ""
    
    // MARK: VGrid logic
    let columns = Array(repeating: GridItem(.flexible()), count: 3)
    
    // MARK: List edit mode
    @State private var isEditing: Bool = false
    
    var body: some View {
        NavigationStack {
            VStack {
                // TODO: ADD FUNCTIONALITY. LATER!!
                Text("")
                    .toolbar {
                        NavigationLink(destination: PaletteCreationView()) {
                            Text("Add")
                        }
                    }
                // GRID OR EMPTY VIEW
                if !userPaletteViewModel.userPaletteColours.isEmpty {
                    // Button to toggle edit mode
                    if isEditing {
                        Button("Done") {
                            isEditing.toggle()
                        }
                        .padding()
                        .background(Color.blue)
                        .foregroundColor(.white)
                        .cornerRadius(8)
                    }
                    
                    List {
                        ForEach(Array(userPaletteViewModel.groupedColours.keys).sorted(), id: \.self) { groupName in
                            if !(userPaletteViewModel.groupedColours[groupName]?.isEmpty ?? false) {
                                VStack(alignment: .leading) {
                                    Text(groupName)
                                        .font(.largeTitle)
                                        .bold()
                                        .padding([.top, .leading], 8)
                                    
                                    // colour list
                                    LazyVGrid(columns: self.columns) {
                                        ForEach(Array(userPaletteViewModel.groupedColours[groupName] ?? [])) { cI in
                                            PaletteListItemView(paletteColourItem: cI)
                                                .onTapGesture {}.onLongPressGesture(minimumDuration: 0.2) { // Setting the // Enable edit mode on long press
                                                    withAnimation {
                                                        isEditing = true
                                                    }
                                                }
                                                .overlay(
                                                    // Show delete button when in edit mode
                                                    isEditing ? Button(action: {
                                                        // Delete action
                                                        if let index = userPaletteViewModel.groupedColours[groupName]?.firstIndex(of: cI) {
                                                            print("tapped to remove \(cI)")
                                                            userPaletteViewModel.groupedColours[groupName]?.remove(at: index)
                                                        }
                                                    }) {
                                                        Image(systemName: "minus.circle.fill")
                                                            .foregroundColor(.red)
                                                    }
                                                        .padding(8)
                                                    : nil,
                                                    alignment: .topTrailing
                                                )
                                        }
                                    
                                    }
                                    .listRowSeparator(.hidden)
                                    .padding()
                                    .searchable(text: $searchText)
                                    .onChange(of: searchText) { search in
                                        if !search.isEmpty {
                                            self.userPaletteViewModel.filterPaletteColours(term: search)
                                        } else {
                                            self.userPaletteViewModel.resetFilteredPaletteColours()
                                        }
                                    }
                                    // end of VGrid
                                }
                                .listRowSeparator(.hidden)
                            } // ForEach

                        }
                    }
                    // colour group header
                } else {
                    //                    EmptyView()
                    VStack(alignment: .center) {
                        Spacer()
                        Text("You have no colours.")
                        Spacer()
                    }
                } // else clause end bracket
            } // end of vstack
            .navigationTitle("Your Palette")
            .onAppear {
                self.userPaletteViewModel.fetchUserPalettes()
            }
        }
        
    }
}

#Preview {
    UserPaletteView()
}
